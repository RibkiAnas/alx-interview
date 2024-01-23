#!/usr/bin/python3
"""Log parsing"""
import sys
import signal


def signal_handler(sig, frame):
    """
      Signal handler for SIGINT
      Args:
        sig: signal number
        frame: stack frame
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """
    Print stats for all status codes in the log file
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {str(code): 0
                    for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            try:
                data = line.split()
                size = int(data[-1])
                status_code = data[-2]

                if status_code in status_codes:
                    status_codes[status_code] += 1
                    total_size += size

                line_count += 1

                if line_count % 10 == 0:
                    print_stats()
            except Exception:
                pass
    except KeyboardInterrupt:
        pass

    print_stats()
