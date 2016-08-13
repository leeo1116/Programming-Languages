import sys
from collections import defaultdict


words = defaultdict(int)
for line in sys.stdin:
    for word in line.split():
        words[word] += 1

for word, count in sorted(words.items()):
    print("{0} was found {1} times".format(word, count))

# To run, type 'python wordcount.py < hamlet.txt' with CMD prompt

# Alternative way:
# import fileinput
# for line in fileinput.input():
#     pass
# To run, type 'python wordcount.py "hamlet.txt"'
