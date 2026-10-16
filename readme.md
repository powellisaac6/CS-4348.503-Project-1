# CS4348 Project 1

## Files
- driver.py: runs logger.py and encryption.py as processes through pipes. It also runs the menu which users write commands to.
- logger.py: logs user and system actions (YYYY-MM-DD HH:MM [ACTION] MESSAGE) 
- encryption.py: PASS, ENCRYPT, DECRYPT, and QUIT commands. Encrypts/decrypts messages, and stores passkeys.
- devlog.md: development log.

## How to run
python3 driver.py log.txt

(On windows: python driver.py log.txt)

Only driver.py needs to be run since it launches the other two programs by itself but all files must be in the same location.

## Notes for the TA
- Inputs are limited to letters only but are case-insensitive.
- Passwords are not written to the log or saved to history.