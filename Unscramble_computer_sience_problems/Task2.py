"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


from collections import defaultdict
from datetime import datetime

if __name__ == '__main__':
    calls_dictionary = defaultdict(int)


for caller, reciever, timestamp, duration in calls:
    date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        calls_dictionary[caller] += int(duration)
        calls_dictionary[reciever] += int(duration)

highest_duration = max(calls_dictionary.items(), key=lambda x: x[1])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*highest_duration))
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

