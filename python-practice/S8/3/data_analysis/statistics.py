def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]

        return (middle1 + middle2) / 2


def standard_deviation(numbers):
    avg = mean(numbers)

    squared_differences = []

    for number in numbers:
        difference = number - avg

    squared_differences.append(difference ** 2)

    variance = sum(squared_differences) / len(numbers)

    return variance ** 0.5