import sys


def main():

    log_file = sys.argv[1]

    with open(log_file, "a"):
        for line in sys.stdin:
            line = line.strip()

            if line == "QUIT":
                break


if __name__ == "__main__":
    main()