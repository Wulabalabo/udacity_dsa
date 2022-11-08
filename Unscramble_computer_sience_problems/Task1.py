"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def getDifferentNumbers()->set:
    diff = set()

    for eachNumbers in [0,1]:
        diff_texts = [data[eachNumbers] for data in texts]
        diff.update(diff_texts)
        diff_calls = [data[eachNumbers] for data in calls]
        diff.update(diff_calls)

    return diff

if __name__ == '__main__':
    differentNumbers = getDifferentNumbers()
    print("There are {0} different telephone numbers in the records.".format(len(differentNumbers)))
