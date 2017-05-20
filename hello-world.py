import time
import sys


python = ["p", "y", "t", "h", "o", "n", ".", ".", ".","🐍"]

print("hello world 🌎")

for item in python:
    print(item, end='')
    sys.stdout.flush()
    time.sleep(0.1)

print()

for i in range(10):
    for j in range(i):
        print(" ", end='')
    print("🐍", end='\r')
    time.sleep(0.1)

time.sleep(0.3)

for j in range(10):
    print(" ", end='')
print()
