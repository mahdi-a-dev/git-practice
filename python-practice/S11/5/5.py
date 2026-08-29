def sum_list(l: list[int]) -> int:
    sum_: int = 0
    for i in l:
        if isinstance(i, int):
            sum_ += i
        else:
            raise TypeError("list must contains only integer values!")
    return sum_

print(sum_list([34, 56.6]))