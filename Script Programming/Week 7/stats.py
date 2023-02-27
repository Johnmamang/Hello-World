"""
File: stats.py
Prints the median and mode of a set of numbers in a file.
"""

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle-1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]


def mode(numbers):
    if not numbers:
        return 0
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    mode = max(counts, key=counts.get)
    if counts[mode] > 1:
        return mode
    else:
        return 0


def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    numbers = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
    print("Numbers:", numbers)
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Mean:", mean(numbers))


if __name__ == '__main__':
    main()
