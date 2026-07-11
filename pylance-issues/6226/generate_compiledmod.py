import os
import py_compile
import tempfile
from pathlib import Path


MODULE_SOURCE = 'VALUE = 1\n'


def main() -> None:
    repo_dir = Path(__file__).resolve().parent
    target = repo_dir / 'compiledmod.pyc'

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'compiledmod.py'
        temp_path.write_text(MODULE_SOURCE, encoding='utf-8')
        py_compile.compile(str(temp_path), cfile=str(target), doraise=True)

    os.utime(target, None)
    print(f'Wrote {target.name}')


if __name__ == '__main__':
    main()