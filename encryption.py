import sys


def main():
    passkey = None

    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        parts = line.split(maxsplit=1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        if command == "QUIT":
            break

        if command == "PASS":
            if not argument:
                print("ERROR Password cannot be empty", flush=True)
            else:
                passkey = argument
                print("RESULT", flush=True)

        elif command == "ENCRYPT" or command == "DECRYPT":
            if passkey is None:
                print("ERROR Password not set", flush=True)
            else:
                print("ERROR No cipher", flush=True)

        else:
            print("ERROR Unknown command", flush=True)


if __name__ == "__main__":
    main()