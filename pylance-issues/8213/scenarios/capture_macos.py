"""Observe selected macOS process identities; never terminate or control the product."""

import argparse
import datetime
import json
from pathlib import Path
import subprocess
import sys
import time


def run(command: list[str]) -> dict:
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return {"command": command, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    except OSError as error:
        return {"command": command, "returncode": None, "stdout": "", "stderr": str(error)}


def snapshot(pylance_pid: int, client_pid: int) -> dict:
    return {
        "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "processes": run([
            "ps", "-ww", "-p", f"{pylance_pid},{client_pid}",
            "-o", "pid=,ppid=,lstart=,etime=,stat=,pcpu=,rss=,command=",
        ]),
        "pylanceIdentity": run(["ps", "-ww", "-p", str(pylance_pid), "-o", "pid=,ppid=,lstart=,stat=,command="]),
        "clientIdentity": run(["ps", "-ww", "-p", str(client_pid), "-o", "pid=,ppid=,lstart=,stat=,command="]),
        "listeners": run(["lsof", "-nP", "-a", "-p", str(pylance_pid), "-iTCP", "-sTCP:LISTEN"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pylance-pid", type=int, required=True)
    parser.add_argument("--client-pid", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--duration", type=float, default=120, help="Observation budget, not a permanent-orphan verdict.")
    parser.add_argument("--interval", type=float, default=2)
    args = parser.parse_args()
    if sys.platform != "darwin":
        parser.error("This helper requires macOS; a Windows run cannot prove the macOS lifecycle.")
    if min(args.pylance_pid, args.client_pid) <= 0 or args.duration <= 0 or args.interval <= 0:
        parser.error("PIDs, duration, and interval must be positive.")
    output = args.output.resolve()
    workspace = Path(__file__).resolve().parents[1]
    if output == workspace or workspace in output.parents:
        parser.error("Raw process captures must be stored outside the publishable workspace.")
    output.mkdir(parents=True, exist_ok=False)
    initial = snapshot(args.pylance_pid, args.client_pid)
    if any(initial[key]["returncode"] != 0 for key in ("pylanceIdentity", "clientIdentity")):
        parser.error("Both selected PIDs must exist before quit. Recheck identities and arguments.")
    print(json.dumps(initial, indent=2), flush=True)
    print("Capture ready. Quit the whole VS Code application with Cmd+Q DURING scanning now.", flush=True)
    print(f"Raw captures remain private until reviewed: {output}", flush=True)
    started = time.monotonic()
    sampled = False
    with (output / "timeline.jsonl").open("x", encoding="utf-8") as timeline:
        state = initial
        while True:
            state["elapsedSeconds"] = round(time.monotonic() - started, 3)
            timeline.write(json.dumps(state) + "\n")
            timeline.flush()
            pylance = state["pylanceIdentity"]
            client = state["clientIdentity"]
            if pylance["returncode"] == 1 and not pylance["stdout"].strip() and not pylance["stderr"].strip():
                print("Selected Pylance PID absent. Inspect timeline/start times before concluding normal exit.")
                break
            if pylance["returncode"] == 0 and client["returncode"] == 1 and not client["stderr"].strip() and not sampled:
                sampled = True
                observation = run(["sample", str(args.pylance_pid), "10", "-file", str(output / "sample.txt")])
                (output / "sample-command.json").write_text(json.dumps(observation, indent=2) + "\n", encoding="utf-8")
            if time.monotonic() - started >= args.duration:
                print("Observation budget reached. Survival is inconclusive, not proof of a permanent orphan.")
                break
            time.sleep(args.interval)
            state = snapshot(args.pylance_pid, args.client_pid)


if __name__ == "__main__":
    main()
