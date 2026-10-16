import subprocess
import sys


def log(logger, action, message=""):
    logger.stdin.write(f"{action} {message}\n")
    logger.stdin.flush()

def encrypt(encryption_program, command):
    encryption_program.stdin.write(command + "\n")
    encryption_program.stdin.flush()
    return encryption_program.stdout.readline().strip()

def check_only_letters(text):
    return text.isascii() and text.isalpha()

def get_txt(history, sys_msg, save_new=True):
    if history:
        choice = input("Use string from history? (y/n): ").strip().lower()
        if choice == "y":
            while True:
                for number, item in enumerate(history, start=1):
                    print(f"{number}. {item}")
                num = input("Enter a number (Enter 0 for new string): ").strip()
                if num == "0":
                    break
                if num.isdigit() and 1 <= int(num) <= len(history):
                    return history[int(num) - 1]
                print("Invalid choice.")

    txt = input(sys_msg).strip()
    if not check_only_letters(txt):
        print("Error: only letters are allowed.")
        return None
    if save_new:
        history.append(txt.upper())
    return txt

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
    encryption_program = subprocess.Popen(
        [sys.executable, "encryption.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    
    history = []
    log(logger, "START", "Driver started")

    while True:
        print()
        print("Commands: password, encrypt, decrypt, history, quit")
        command = input("Enter a command: ").strip().lower()
 
        if command == "quit":
            log(logger, "COMMAND", "quit")
            break
 
        elif command == "history":
            log(logger, "COMMAND", "history")
            if not history:
                print("History is empty.")
            for number, item in enumerate(history, start=1):
                print(f"{number}. {item}")
 
        elif command == "password":
            log(logger, "COMMAND", "password")
            txt = get_txt(history, "Enter a password: ", False)
            if txt is None:
                log(logger, "ERROR", "Password must contain only letters")
            else:
                reply = encrypt(encryption_program, "PASS " + txt.upper())
                if reply.startswith("RESULT"):
                    print("Password set.")
                    log(logger, "RESULT", "Password set")
                else:
                    print(reply)
                    log(logger, "ERROR", reply)

        elif command in ("encrypt", "decrypt"):
            log(logger, "COMMAND", command)
            txt = get_txt(history, f"Enter a string to {command}: ")
            if txt is None:
                log(logger, "ERROR", "Input must contain only letters")
            else:
                reply = encrypt(encryption_program, command.upper() + " " + txt.upper())
                if reply.startswith("RESULT"):
                    result = reply[len("RESULT"):].strip()
                    print(f"Result: {result}")
                    history.append(result)
                    log(logger, "RESULT", result)
                else:
                    print(reply)
                    log(logger, "ERROR", reply)
 
        else:
            log(logger, "ERROR", "Unknown command")
            print("Unknown command.")

    log(logger, "EXIT", "Driver exiting")

    encryption_program.stdin.write("QUIT\n")
    encryption_program.stdin.flush()
    logger.stdin.write("QUIT\n")
    logger.stdin.flush()

    encryption_program.wait()
    logger.wait()


if __name__ == "__main__":
    main()