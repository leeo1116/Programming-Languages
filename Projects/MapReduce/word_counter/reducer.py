import sys


def output(previous_key, total):
    if previous_key:
        print("{0} was found {1} times".format(previous_key, total))

previous_key = None
total = 0

for line in sys.stdin:
    key, value = line.split("\t", 1)
    if key != previous_key:
        output(previous_key, total)
        previous_key = key
        total = 0
    total += int(value)

output(previous_key, total)

# To run MapReduce, type 'type hamlet.txt | python mapper.py | sort | python reducer.py'
# '|' redirects the output from 'type hamlet.txt' which is similar to unix 'cat hamlet.txt'. it send the hamlet.txt to
# standard output (screen by default). If '|' is used, then it redirects the output from 'type hamlet.txt' to
# 'mapper.py'as input arguments

# Try 'type hamlet.txt' first, and then 'type hamlet.txt | python mapper.py', then 'type hamlet.txt | python mapper.py |
# sort'. Sort function will sort all the output from the previous output. Finally try type hamlet.txt | python mapper.py
#  | sort | python reducer.py
