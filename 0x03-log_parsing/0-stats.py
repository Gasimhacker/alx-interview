#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import sys
import re
import signal


ip = r'(\d{1-3}\.){3}\d{1-3}'
http_request = r'\"GET /projects/260 HTTP/1.1\"'
status_code_r = r' 200 | 301 | 400 | 401 | 403 | 404 | 405 | 500 '
file_size_r = r'\d*$'
date = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]'
pattern = f'{ip} - {date} {http_request}{status_code_r}{file_size_r}'

fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
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


def handler(signum, frame):
    """Call print_stats again when ctrl+c is pressed"""
    print_stats()


signal.signal(signal.SIGINT, handler)


for line in sys.stdin:
    count += 1
    m = re.fullmatch(log_fmt, line)
    if m:
        status_code = m.group('status_code')
        file_size = int(m.group('file_size'))
        status_codes[status_code] += 1
        total_size += file_size

    if count % 10 == 0:
        print_stats()
