#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
It prints the total file size and the number of lines by status code
every 10 lines or after a keyboard interruption (CTRL + C).
"""
import re
import sys

status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
total_size = 0
line_count = 0

line_pattern = r'^(\d+\.\d+\.\d+\.\d+).*\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$'
line_regex = re.compile(line_pattern)


def print_metrics():
    """
    Prints the total file size and the number of lines by status code.
    """
    global total_size, status_codes

    print(f"File size: {total_size}")
    sorted_codes = sorted(status_codes.items(), key=lambda x: x[0])
    for code, count in sorted_codes:
        if count > 0:
            print(f"{code}: {count}")


def update_metrics(line):
    """
    Updates the metrics based on the input line.
    """
    global total_size, status_codes, line_count

    match = line_regex.match(line)
    if match:
        ip, date, status_code, file_size = match.groups()
        total_size += int(file_size)
        status_codes[status_code] += 1

    line_count += 1
    if line_count % 10 == 0:
        print_metrics()


try:
    for line in sys.stdin:
        update_metrics(line)
except KeyboardInterrupt:
    print_metrics()
    raise
