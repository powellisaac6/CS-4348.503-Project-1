import sys


def main():

    log_file = sys.argv[1]

    with open(log_file, "a"):
        for line in sys.stdin:
            line = line.strip()

            if line == "QUIT":
                break

            if not line:
                continue

            substrings = line.split(maxsplit=1)
            action = substrings[0]
            message = substrings[1] if len(substrings) > 1 else ""

            print("Action:", action)
            print("Message:", message)


if __name__ == "__main__":
    main()