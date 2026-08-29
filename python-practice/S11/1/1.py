
def sum_list(l: list[int | float]) -> float | int:
    sum_ = 0
    for i in l:
        try:
            sum_+= i
        except TypeError:
            print("list must contains only int and float value.")
    return sum_


print(sum_list([4, 10, 12.5, 8, 5, "4", "2"]))