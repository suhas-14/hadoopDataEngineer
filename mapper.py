import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(f'{word}\t1')

# This script reads lines from standard input, splits each line into words, and
# prints a tab-separated line for each word, with the word and a count of 1.
# The output is written to standard output.