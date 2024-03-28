#!/usr/bin/python3
import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

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