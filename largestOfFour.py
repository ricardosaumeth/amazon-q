InnerArray = list[float]
Numbers = list[InnerArray]


def largest_of_four(numbers: Numbers) -> list[float]:
    return [max(arr) for arr in numbers]


print(
    largest_of_four([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
)  # [4, 8, 12, 16]
