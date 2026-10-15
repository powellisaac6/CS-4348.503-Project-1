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