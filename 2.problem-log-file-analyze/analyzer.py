import re
from collections import defaultdict


LOG_FILE = "logs/access.log"


LOG_PATTERN = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] '
    r'"(?P<method>\w+) (?P<path>[^\s]+) HTTP/1.1" (?P<status>\d+) \d+'
)

def parse_log(file_path):
    ip_count = defaultdict(int)
    page_count = defaultdict(int)
    status_count = defaultdict(int)

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)
            if match:
                ip = match.group("ip")
                path = match.group("path")
                status = match.group("status")

                ip_count[ip] += 1
                page_count[path] += 1
                status_count[status] += 1

    return ip_count, page_count, status_count

def display_results(ip_count, page_count, status_count):
    print("\n=== Request Count by IP ===")
    for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip}: {count}")

    print("\n=== Most Requested Pages ===")
    for page, count in sorted(page_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{page}: {count}")

    print("\n=== Status Code Frequencies ===")
    for status, count in sorted(status_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{status}: {count}")

def main():
    print("Parsing log file...")
    ip_count, page_count, status_count = parse_log(LOG_FILE)
    display_results(ip_count, page_count, status_count)

if __name__ == "__main__":
    main()
