# CS4348 Project 1

## Files
- driver.py: runs logger.py and encryption.py as processes through pipes. It also runs the command menu.
- logger.py: logs actions the user makes (YYYY-MM-DD HH:MM [ACTION] MESSAGE) 
- encryption.py: PASS, ENCRYPT, DECRYPT, and QUIT commands. Allows user to encrypt, decrypt, and to make passwords.
- devlog.md: development log.

## How to run
python3 driver.py log.txt

Only driver.py needs to be ran since it launches the other two programs by itself but all files must be in the same location.

## Notes for the TA
- Inputs are limited to letters only but are case-insensitive.
- Passwords are not saved to history.