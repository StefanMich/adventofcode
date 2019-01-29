import re
from datetime import datetime
from enum import Enum

with open('day_4_testinput') as f:
    input_strings = f.read()


class EntryType(Enum):
    begin_shift, falls_asleep, wakes_up = range(3)

    @staticmethod
    def convert(message):
        if 'wakes' in message:
            return EntryType.wakes_up
        elif 'asleep' in message:
            return EntryType.falls_asleep
        elif 'Guard' in message:
            return EntryType.begin_shift


class LogEntry:
    guard_number = ''

    def __init__(self, entry_datetime, message):
        self.entry_datetime = entry_datetime
        self.message = message
        self.entry_type = EntryType.convert(message)
        if self.entry_type == EntryType.begin_shift:
            regex = re.compile('.*#(\d+).*')
            parsed = regex.search(message)
            self.guard_number = parsed.group()

    def __str__(self):
        return f"{self.entry_datetime}: {self.message} " \
            f"- {self.entry_type} - {self.guard_number}"


log_entries = []
for line in input_strings.split('\n'):
    if not line:
        continue

    regex = re.compile(
        r'\[(?P<year>\d+)-(?P<month>\d+)-(?P<date>\d+) '
        r'(?P<hour>\d+):(?P<minute>\d+)\](?P<message>.*)'
    )
    parsed = regex.search(line)

    line_datetime = datetime(
        int(parsed.group('year')),
        int(parsed.group('month')),
        int(parsed.group('date')),
        int(parsed.group('hour')),
        int(parsed.group('minute')),
    )
    message = parsed.group('message')

    log_entries.append(LogEntry(line_datetime, message))

shifts = dict()
guard = None
start_minute = None

log_entries.sort(key=lambda entry: entry.entry_datetime)
for entry in log_entries:
    if entry.entry_type == EntryType.begin_shift:
        guard = entry.guard_number
        start_minute = entry.entry_datetime.minute

    if entry.entry_type == EntryType.falls_asleep
    print(entry)
