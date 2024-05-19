import time


def main():
    start = time.time() * 1000

    count = 0
    number = 50_000_000

    for i in range (number):
        count += 1

    duration = int(round(time.time() * 1000 - start))

    print(f"Counting to {number} in Python took {duration} ms.")


if __name__ == "__main__":
    main()
