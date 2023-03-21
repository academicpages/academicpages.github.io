from io import TextIOWrapper
import sys
import argparse
import os

os.system("color")
from pathlib import Path
import re

parser = argparse.ArgumentParser(description="Parse a test log into its parts")
parser.add_argument("testlog", type=str, nargs=1, help="Log to parse")
parser.add_argument(
    "--testoutput", action="store_true", help="Show all failures and passes"
)
parser.add_argument(
    "--split",
    action="store_true",
    help="Split into per process files. Each file will have the pid appended",
)
ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
pid_regex = re.compile(r"(\d+).*")
timestamp_regex = re.compile(r"\d{4}-\d{2}-\d{2}T.*\dZ")


def stripTimestamp(line: str):
    match = timestamp_regex.match(line)
    if match:
        return line[match.end() :]
    return line


def readStripLines(f: TextIOWrapper):
    return map(stripTimestamp, f.readlines())


def printTestOutput(testlog):
    # Find all the lines that don't have a PID in them. These are the test output
    p = Path(testlog[0])
    with p.open() as f:
        for line in readStripLines(f):
            stripped = line.strip()
            if len(stripped) > 2 and stripped[0] == "\x1B" and stripped[1] == "[":
                print(line.rstrip())  # Should be a test line as it has color encoding


def splitByPid(testlog):
    # Split testlog into prefixed logs based on pid
    baseFile = os.path.splitext(testlog[0])[0]
    p = Path(testlog[0])
    pids = set()
    logs = {}
    pid = None
    with p.open() as f:
        for line in readStripLines(f):
            stripped = ansi_escape.sub("", line.strip())
            if len(stripped) > 0:
                # Pull out the pid
                match = pid_regex.match(stripped)

                # Pids are at least two digits
                if match and len(match.group(1)) > 2:
                    # Pid is found
                    pid = int(match.group(1))

                    # See if we've created a log for this pid or not
                    if not pid in pids:
                        pids.add(pid)
                        logFile = "{}_{}.log".format(baseFile, pid)
                        print("Writing to new log: " + logFile)
                        logs[pid] = Path(logFile).open(mode="w")

                # Add this line to the log
                if pid != None:
                    logs[pid].write(line)
    # Close all of the open logs
    for key in logs:
        logs[key].close()


def doWork(args):
    if not args.testlog:
        print("Test log should be passed")
    elif args.testoutput:
        printTestOutput(args.testlog)
    elif args.split:
        splitByPid(args.testlog)
    else:
        parser.print_usage()


def main():
    doWork(parser.parse_args())


if __name__ == "__main__":
    main()
