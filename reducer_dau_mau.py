import sys

currentKey = None
userSet = set()

for line in sys.stdin:
    key , user_id = line.strip().split("\t")

    if key != currentKey:
        if currentKey is not None:
            print(f"{currentKey}\t{len(userSet)}")
        currentKey = key
        userSet = set()

    userSet.add(user_id)

if currentKey is not None:
    print(f"{currentKey}\t{len(userSet)}")