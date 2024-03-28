#!/usr/bin/python3
"""
This script reads from stdin line by line and computes metrics.
The input format is specified and after every 10 lines or a keyboard interruption (CTRL + C),
it prints statistics from the beginning.
"""

import sys
import signal

def signal_handler(sig, frame):
    """
    Handles the signal interruption (CTRL + C), prints the statistics and exits.
    """
    print_stats()
    sys.exit(0)

def print_stats():
    """
    Prints the total file size and the number of lines by status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Initialize status codes dictionary, total size and line count
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

# Set up the signal handler for the SIGINT signal (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            data = line.split()
            total_size += int(data[-1])
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
        except:
            pass
        if line_count == 9:
            print_stats()
            line_count = -1
        line_count += 1
except KeyboardInterrupt:
    print_stats()
    raise