from typing import Optional, Union
import math


def validate_numbers(numbers: list[float]):
    if not numbers:
        raise ValueError("List cannot be empty")


def binary_search(numbers: list[float], target: Union[int, float]) -> Optional[int]:
    validate_numbers(numbers)
    numbers = sorted(numbers)
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = math.floor((left + right) / 2)
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
