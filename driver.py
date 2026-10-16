import subprocess
import sys


def log(logger, action, message=""):
    logger.stdin.write(f"{action} {message}\n")
    logger.stdin.flush()


def main():
    if len(sys.argv) != 2:
        print("Error! Provide log file name.")
        print("Example: python driver.py log.txt")
        sys.exit(1)

    log_file = sys.argv[1]

    logger = subprocess.Popen(
        [sys.executable, "logger.py", log_file],
        stdin=subprocess.PIPE,
        text=True,
    )

    log(logger, "START", "Driver started")
    log(logger, "EXIT", "Driver exiting")

    logger.stdin.write("QUIT\n")
    logger.stdin.flush()
    logger.wait()


if __name__ == "__main__":
    main()