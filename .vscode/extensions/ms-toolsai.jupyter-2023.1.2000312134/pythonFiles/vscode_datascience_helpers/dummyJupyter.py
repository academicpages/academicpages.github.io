# This file can mimic juypter running. Useful for testing jupyter crash handling

import sys
import argparse
import time


def main():
    print("hello from dummy jupyter")
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", type=bool, default=False, const=True, nargs="?")
    parser.add_argument("notebook", type=bool, default=False, const=True, nargs="?")
    parser.add_argument("--no-browser", type=bool, default=False, const=True, nargs="?")
    parser.add_argument("--notebook-dir", default="")
    parser.add_argument("--config", default="")
    results = parser.parse_args()
    if results.version:
        print("1.1.dummy")
    else:
        print(
            "http://localhost:8888/?token=012f08663a68e279fe0a5335e0b5dfe44759ddcccf0b3a56"
        )
        time.sleep(5)
        raise Exception("Dummy is dead")


if __name__ == "__main__":
    main()
