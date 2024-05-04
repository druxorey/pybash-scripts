import time

start = time.time()

count = 0
number = 50_000_000

for i in range (number):
    count += 1

duration = time.time() - start

print(f"Counting to {number} in Python took {duration} seconds")
