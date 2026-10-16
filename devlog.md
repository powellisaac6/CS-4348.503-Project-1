# 10-12-2026 11:50 PM

First entry of the first session.
I am going to do a basic implementation of logger.py first.

I will start by having the code read the first argument (the log filename) from the command line.
The log filename will be stored as a string in the variable log_file.
The code will open a log file using the log_file variable.
It will then read a typed line from the command line and remove the whitespace at the beginning and end of the string.
For now, I will make the code exit if the phrase "QUIT" is typed.
Commands will be sent through a pipe later on.

python logger.py log.txt runs the program.

I type QUIT and the program exits.
Everything works.

# 10-13-2026 12:50 AM

NOTE: Working past midnight, still session 1.

This time I want the code to read an action and a message with it.
Later on, the driver will be sending these messages through a pipe to the logger.

For instance, START Logging started will be sent from the driver and the logger will log it as [START] Logging Started.

For now, I want to type these commands in the command line.
I am going to have the program split the individual words from the command line. 
The first word will be action being performed.
The rest will be the message describing the action.
I'm going to have the action and the message print on the command line for testing purposes.

I am going to test "start logging started" as a command.
You can view the result below.

Action: start

Message: logging started

End of session 1. Next session I would like to get logger.py writing to the log file. 

NOTE: A few general errors pushed me past the original time: Gitignore was not working properly and there were some wording/formatting errors in the devlog. Not enough to make a new entry. Ran git rm --cached log.txt in my command line to stop tracking. Everything is fixed now.

# 10-13-2026 12:28 PM

This session I want to make logger.py write to the log file now.
I'll remove the command line print.
Instead I want it to output write to the log file.
I'll have it print as such: 

[action] message

To avoid buffer delays I'll add the output.flush() command.

Now to test I'll write to the command "START Logging started" and "ENCRYPT Text encrypted" to the command line.

The log file:

[START] Logging started

[ENCRYPT] Text encrypted

Works as intended.

# 10-13-2026 1:46 PM

Next I'm going to add timestamp recording to logger.py.

datetime.now() will get the date from the local system.

strftime("%Y-%m-%d %H:%M") will put it in the correct format.

Now all there is left to do is output it before the action and message. 
Here is the result: 

2026-10-13 13:22 [ENCRYPT] Text encrypted

I want logger.py to do some error handling in case a log file isn't given as an argument.
So, if a filename is not given as an argument, then the program will stop and provide an error message. Testing result below.

python logger.py

Error! Provide log file name.

Example: python logger.py log.txt

The major functional operations for logger.py have been completed. This concludes session 2. 
Next session, I would like to start programming message encryption.

# 10-15-2026 4:33 PM

This session I will create basic command recognition for encryption.py.
I will start with making a passkey variable.
I'll use the same line handling I used in logger.py. 
Command/argument will be used to describe the string split instead of action/message. 
QUIT will exit the program as usual.
PASS will only store a string in the passkey variable for now and nothing else. 
Basic error handling for PASS will prevent empty strings.
ENCRYPT and DECRYPT commands will be recognized but will do nothing for now. 
I will implement the Vigenère cipher in the second half of this session.
If the password has not been set, the ENCRYPT and DECRYPT commands will return errors. 
The code also will return errors if an unknown command is given. 

encryption.py reads directly from stdin and writes directly to stdout.
Later on, the driver will use a separate process to run encryption.py and connect these streams using pipes.
flush=True will be added to each print statement so the output can be sent directly through a pipe.
If not used, the stream could sit in the buffer forever.

Here's an example of how the code functions:

User: PASS

System: ERROR Passkey cannot be empty

User: ENCRYPT HELLO

System: ERROR Password not set

User: PASS HELLO

System: RESULT

User: ENCRYPT HELLO

System: ERROR No cipher

User: DAJKFDK

System: ERROR Unknown command

User: QUIT

The first goal of this session was to create a basic skeleton of encryption.py that recognizes commands.
No significant errors occurred given the simplicity.
The next entry will expand on the actual functionality of each command.

# 10-15-2026 6:20 PM

I plan on implementing the Vigenère cipher now. Understanding how it worked was a little bit confusing at first but after going over the project guidelines and drawing it out, I can comprehend how to move forward and begin coding.

I found that first I need to convert each letter of the passkey and each letter of the message I'm encrypting/decrypting into a number.
A = 0, B = 1, C = 2, ... , Z = 25.
A loop will go through each letter of the passkey and the message.
For ENCRYPT, each letter in the passkey will be converted to a number. The letter in the message at the same index will shift right by that number.
For DECRYPT, each letter in the passkey will be converted to a number. The letter in the message at the same index will shift left by that number.

How it works:

Passkey: H

Message: H

H = 7

7 + 7 = 14

O = 14

Encrypted Message: O

I will insert % 26 in case an index reaches a value greater than 25 or less than 0.
It will wrap around in such cases. 

If the passkey is shorter than the message, the passkey will just repeat.

Example: 

Passkey: HELLO

Message: HELLOOO

New passkey: HELLOHE

I will now make it so the encrypt and decrypt commands run the Vigenère cipher. A new error is given if no string is passed to process.

User: ENCRYPT HELLO

System: ERROR Password not set

User: PASS HELLO

System: RESULT

User: ENCRYPT HELLO

System: RESULT OIWWC

User: DECRYPT OIWWC

System: RESULT HELLO

User: ENCRYPT

System: ERROR Nothing to encrypt/decrypt

User: DECRYPT

System: ERROR Nothing to encrypt/decrypt

User: QUIT

Everything works. 
Next session I will begin the driver program.

# 10-15-2026 7:10 PM

This session I'm going to implement driver.py.
I'm going to start by connecting it to logger.py through a pipe.
I'll use the same logic for starting up logger.py requiring a log filename entry as an argument.

driver.py will then open a pipe to logger.py using subprocess.Popen().
stdin=subprocess.PIPE allows the driver to write to the logger's stdin.
logger.py will log the start and exit messages from the driver.
Lastly, driver.py will issue a quit command to the logger using the pipe.
flush() is used again to ensure no output gets stuck in the buffer.
wait() makes it so the driver can't exit until the logger is finished.

Running the python driver.py log.txt results in this in the log file:

2026-10-15 19:02 [START] Driver started

2026-10-15 19:02 [EXIT] Driver exiting

Everything works.

# 10-15-2026 7:50 PM

I'm going to add a menu loop now.
I'll start the loop directly in between the driver start and exit log commands.
Before the loop, I'm going to add an array to track history.
In the loop, I'll have the program give the user a list of commands (password, encrypt, decrypt, history, quit).
The input should be case insensitive and strip any unnecessary white space automatically so strip() and lower() will be used.
I'll have each command be logged using the logger's pipe.
No command functionality yet.

I'm not sure why I just now thought of this but I almost forgot to implement the encryption program's pipe. 
Inserting after creating the menu loop may be a bit wonky.
I'll just copy what I did for logger.py for the most part.

I tested a few commands:

2026-10-15 19:21 [START] Driver started

2026-10-15 19:21 [COMMAND] history

2026-10-15 19:21 [COMMAND] history

2026-10-15 19:22 [ERROR] Unknown command

2026-10-15 19:22 [COMMAND] encrypt

2026-10-15 19:22 [COMMAND] quit

2026-10-15 19:22 [EXIT] Driver exiting

Everything works as intended.

Next session, I would like to have each command to be fully functional.