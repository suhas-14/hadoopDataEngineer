import sys

currentWord = None
wordCount = 0

for line in sys.stdin:
    word, wordCount = line.strip().split('\t')
    count = int(wordCount)

    if word == currentWord:
        wordCount += word
    else:
        if currentWord:
            print(f"{currentWord}\t{wordCount}")
        currentWord = word
        wordCount = count

if currentWord:
    print(f"{currentWord}\t{wordCount}")