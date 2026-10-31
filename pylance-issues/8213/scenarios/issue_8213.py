"""Generate original Python files to model the reported large-workspace scan trigger."""

import argparse
import json
from pathlib import Path


MARKER = ".issue_8213_synthetic.json"
WORKSPACE_ROOT = Path(__file__).resolve().parents[1]


def module_text(group: int, module: int) -> str:
    return (
        '"""Original synthetic input for a workspace traversal/shutdown check."""\n\n'
        f"MODULE_NAME = 'group_{group:04d}.module_{module:04d}'\n"
        f"OFFSET = {group * 1000 + module}\n\n"
        "def make_record(value: int) -> dict[str, int | str]:\n"
        "    return {'name': MODULE_NAME, 'value': value + OFFSET}\n"
    )


def put_file(path: Path, text: str) -> None:
    if path.exists():
        if path.is_symlink() or path.read_text(encoding="utf-8") != text:
            raise ValueError(f"Refusing to overwrite an unexpected file: {path}")
        return
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)


def generate(workspace_root: Path, groups: int, modules: int) -> dict:
    if groups < 1 or modules < 1 or groups * modules > 262144:
        raise ValueError("Require positive dimensions and at most 262144 modules.")
    tree = workspace_root / "scan_tree"
    marker = tree / MARKER
    if tree.is_symlink():
        raise ValueError("Refusing to write through a scan_tree symlink.")
    if tree.exists() and not marker.is_file():
        raise ValueError("Existing scan_tree is not marked as this synthetic fixture.")
    if marker.is_file():
        previous = json.loads(marker.read_text(encoding="utf-8"))
        if groups < previous["groups"] or modules < previous["modulesPerGroup"]:
            raise ValueError("Expansion only: use dimensions at least as large as the existing fixture.")
        if any(path.is_symlink() for path in tree.rglob("*")):
            raise ValueError("Refusing to expand a tree containing symlinks.")
    tree.mkdir(parents=True, exist_ok=True)
    put_file(tree / "__init__.py", '"""Original synthetic scan workspace."""\n')
    for group in range(groups):
        group_dir = tree / f"group_{group:04d}"
        group_dir.mkdir(exist_ok=True)
        put_file(group_dir / "__init__.py", '"""Synthetic group package."""\n')
        for module in range(modules):
            batch_dir = group_dir / f"batch_{module // 16:04d}"
            batch_dir.mkdir(exist_ok=True)
            put_file(batch_dir / "__init__.py", '"""Synthetic batch package."""\n')
            put_file(batch_dir / f"module_{module:04d}.py", module_text(group, module))
    result = {
        "issueUrl": "https://github.com/microsoft/pylance-release/issues/8213",
        "synthetic": True,
        "groups": groups,
        "modulesPerGroup": modules,
        "moduleCount": groups * modules,
        "batchCount": groups * ((modules + 15) // 16),
    }
    marker.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def check(workspace_root: Path) -> dict:
    tree = workspace_root / "scan_tree"
    result = json.loads((tree / MARKER).read_text(encoding="utf-8"))
    paths = list(tree.rglob("*"))
    if any(path.is_symlink() for path in paths):
        raise ValueError("Unexpected symlink in synthetic fixture.")
    modules = [path for path in paths if path.name.startswith("module_") and path.suffix == ".py"]
    expected_py = result["moduleCount"] + result["groups"] + result["batchCount"] + 1
    if len(modules) != result["moduleCount"] or sum(path.suffix == ".py" for path in paths) != expected_py:
        raise ValueError("Generated Python-file counts do not match the recorded fixture dimensions.")
    for group in range(result["groups"]):
        for module in range(result["modulesPerGroup"]):
            path = tree / f"group_{group:04d}" / f"batch_{module // 16:04d}" / f"module_{module:04d}.py"
            if path.read_text(encoding="utf-8") != module_text(group, module):
                raise ValueError(f"Generated module does not match: {path}")
    return {**result, "checkedPythonFiles": expected_py}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--groups", type=int, default=256)
    parser.add_argument("--modules-per-group", type=int, default=128)
    parser.add_argument("--check", action="store_true", help="Validate the currently materialized fixture.")
    args = parser.parse_args()
    result = check(WORKSPACE_ROOT) if args.check else generate(WORKSPACE_ROOT, args.groups, args.modules_per_group)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
