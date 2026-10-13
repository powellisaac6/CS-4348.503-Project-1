# 10-12-2026 11:50 PM
First entry of the first session.
I am doing a basic implementation of logger.py first.
I start with having the code read the first argument (the log filename) from the command line.
The log filename will be stored as a string in the variable log_file.
I am now going to have the code open the log file using the log_file variable.
I will have the code read in a typed line on the command line and remove whitespace.
For now, I will make the code exit if the phrase "QUIT" is typed.
Commands will be sent through a pipe later on.

python logger.py log.txt runs the program.
I type QUIT and the program exits.
Everything works.

# 10-13-2026 12:36 AM
NOTE: Worked past midnight, still session 1.
This time I wanted the code to read an action and a message with it
Later on, the driver will be sending these messages through a pipe to the logger.
For instance, START Logging started will be sent from the driver and the logger will log it as [START] Logging Started.

For now, I want to type these commands in through the command line.
I am going to have the program split the individual words from the command line. 
The first word will be action being performed.
The rest will be the message describing the action.
I'm going to have the action and the message print to the command line for testing purposes.

I am going to test "start logging started" as a command.
Result below.

Action: start
Message: logging started

End of session 1. Next session I would like to get logger.py writing to the log file.