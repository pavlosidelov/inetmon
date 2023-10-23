# inetmon
Internet Availability Monitor and Logger

This Python program continuously checks internet availability by trying to contact a global website like Google. If the internet is available, a simple timestamp is written to the console. If the internet goes down, a special message with a timestamp is written to a log file. When the internet comes back online, another special message with a timestamp is written to the log file.

This program can be used to log internet availability and provide proof to an internet provider's technical team if you are experiencing unstable internet service.

Usage

To run the program, simply open a terminal window and navigate to the directory where the program is located. Then, run the following command:

"python inetmon.py"

There are two main ways to run a Python program in the background after the terminal window is closed:

Use the "nohup" command.
The "nohup" command tells the shell to ignore the hangup signal (SIGHUP), which is sent when the terminal window is closed. To run a Python program in the background using "nohup", simply prefix the command with "nohup". For example, to run the Python program my_script.py in the background, you would use the following command:

"nohup python my_script.py &"

The & at the end of the command tells the shell to run the program in the background.

The program will start running in the background and will continuously check internet availability. To view the log file, you can use a text editor such as nano or vim.

Example log file:
2023-10-12, 09:37:41, Event, Service Started
2023-10-12, 10:16:11, Event, Internet Down
2023-10-12, 10:16:16, Event, Internet Restored

You can configure the program with the next section in the code:
#----------CONFIGURATION START--------------------
#Change this Log file name to whatever you want
LOG_FILE = "internet_status_log.txt"

#Change this URL to enything else you want to check availability
CHECK_URL = "https://www.google.com"

#Change this interval to whatever you want
CHECK_INTERVAL = 5  # seconds
#----------CONFIGURATION END--------------------

Copyright (c) 2023 Pavlo Sidelov www.sidelov.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
