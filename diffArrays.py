def diff_arrays(array1: list[int], array2: list[int]):

    smallest, largest = (
        (array1, array2) if len(array1) <= len(array2) else (array2, array1)
    )
    # return [x for x in largest if x not in smallest]
    return list(filter(lambda x: x not in smallest, largest))


print(diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5]))  # 4
print(diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5, 6]))  # 4,6
