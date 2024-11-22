def validate_numbers(numbers: list[int]):
    if not numbers:
        raise ValueError("numbers must be valid and not empty")

def destroyer(numbers: list[int], target1: int, target2: int):
    validate_numbers(numbers)
    # return [x for x in numbers if x != target1 and x != target2]
    # return list(x for x in numbers if x != target1 and x != target2)
    return list(filter(lambda x: x != target1 and x != target2, numbers))


print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))  # [1, 1]
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))  # [1, 5, 1]
