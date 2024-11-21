def validate_array(numbers: list[int]):
    if not isinstance(numbers, list):
        raise ValueError("input must be a valid list of integers")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("all elements in numbers must be numeric")


def diff_arrays(array1: list[int], array2: list[int]):
    validate_array(array1)
    validate_array(array2)

    smallest, largest = (
        (array1, array2) if len(array1) <= len(array2) else (array2, array1)
    )
    # return [x for x in largest if x not in smallest]
    return list(filter(lambda x: x not in smallest, largest))


print(diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5]))  # 4
print(diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5, 6]))  # 4,6
