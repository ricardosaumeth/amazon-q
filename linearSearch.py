def linear_search(numbers: list[float], target: float) -> int:
    if not isinstance(numbers, list):
        raise ValueError("Input must be valid numbers")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be valid numbers")
    if not isinstance(target, (int, float)):
        raise ValueError("Target must be a valid number")
    # found = -1
    # for i, x in enumerate(numbers):
    #     if x == target:
    #         found = i
    #         break
    # return found
    try:
        return numbers.index(target)
    except ValueError:
        return -1


print(linear_search([1, 2, 3, 49, 5], 490))  # -1
print(linear_search([1, 2, 3, 49, 5], 49))  # 3
