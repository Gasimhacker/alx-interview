#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import sys
import re


ip = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
http_request = r'\"GET /projects/260 HTTP/1.1\"'
status_code_r = r'(?P<status_code>200|301|400|401|403|404|405|500)'
file_size_r = r'(?P<file_size>\d+$)'
date = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]'
pattern = f'{ip} - {date} {http_request} {status_code_r} {file_size_r}'

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0
                }
total_size = 0
count = 0


def print_stats():
    """Print the stats after collecting it from stdin"""
    print(f'File size: {total_size}', flush=True)
    [print(f'{code}: {count}', flush=True)
        for code, count in status_codes.items() if count > 0]


try:
    while True:
        line = input()
        count += 1
        m = re.fullmatch(pattern, line)
        if m:
            status_code = m.group('status_code')
            file_size = int(m.group('file_size'))
            status_codes[status_code] += 1
            total_size += file_size

        if count % 10 == 0:
            print_stats()
except (KeyboardInterrupt, EOFError):
    print_stats()
