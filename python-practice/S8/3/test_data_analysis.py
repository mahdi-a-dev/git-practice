from data_analysis import statistics

numbers = list(map(float, input("Enter a list (split with , ): ").split(",")))

print(f"mean: {(statistics.mean(numbers)):.2f}")
print(f"medain: {(statistics.median(numbers)):.2f}")
print(f"standard deviaion: {(statistics.standard_deviation(numbers)):.2f}")