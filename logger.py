import sys
from datetime import datetime


def main():

    if len(sys.argv) != 2:
        print("Error! Provide log file name.")
        print("Example: python logger.py log.txt")
        sys.exit(1)

    log_file = sys.argv[1]

    with open(log_file, "a") as output:
        for line in sys.stdin:
            line = line.strip()

            if line == "QUIT":
                break

            if not line:
                continue

            substrings = line.split(maxsplit=1)
            action = substrings[0]
            message = substrings[1] if len(substrings) > 1 else ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            output.write(f"{timestamp} [{action}] {message}\n")
            output.flush()


if __name__ == "__main__":
    main()