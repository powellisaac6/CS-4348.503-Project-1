import sys

def vigenere(text, key, decrypt=False):
    result = ""
    for i, char in enumerate(text):
        shift = ord(key[i % len(key)]) - ord("A")
        if decrypt:
            shift = -shift
        result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    return result

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
                print("ERROR Passkey cannot be empty", flush=True)
            else:
                passkey = argument
                print("RESULT", flush=True)

        elif command == "ENCRYPT" or command == "DECRYPT":
            if passkey is None:
                print("ERROR Password not set", flush=True)
            elif not argument:
                print("ERROR Nothing to encrypt/decrypt", flush=True)
            else:
                text = argument.upper()
                key = passkey.upper()
                result = vigenere(text, key, decrypt=(command == "DECRYPT"))
                print("RESULT", result, flush=True)
        else:
            print("ERROR Unknown command", flush=True)


if __name__ == "__main__":
    main()