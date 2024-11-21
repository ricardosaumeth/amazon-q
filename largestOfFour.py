from typing import List, Tuple

InnerArray = Tuple[float, float, float, float]
Numbers = List[InnerArray]


def largest_of_four(numbers: Numbers) -> List[float]:
    if not isinstance(numbers, List):
        raise ValueError("List must be of type Numbers")
    if not all(isinstance(x, List) for x in numbers):
        raise ValueError("All elements mus be either int of float")
    return [max(arr) for arr in numbers]


print(
    largest_of_four([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
)  # [4, 8, 12, 16]
