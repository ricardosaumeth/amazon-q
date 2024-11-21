def validate_numbers(numbers: list[int], target1: int, target2: int):
    if not isinstance(numbers, list) or not numbers:
        raise ValueError("numbers must be valid and not empty")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("all elements in numbers must be numeric")
    if not isinstance(target1, (int, float)) or not isinstance(target2, (int, float)):
        raise ValueError("Target input mus be valid")


def destroyer(numbers: list[int], target1: int, target2: int):
    validate_numbers(numbers, target1, target2)
    # return [x for x in numbers if x != target1 and x != target2]
    # return list(x for x in numbers if x != target1 and x != target2)
    return list(filter(lambda x: x != target1 and x != target2, numbers))


print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))  # [1, 1]
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))  # [1, 5, 1]
