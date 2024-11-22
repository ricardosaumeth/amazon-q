def chunk(numbers: list[float], size: int) -> list[list[float]]:
    if size > 0:
        raise ValueError("Size must be a positive value")
    if not numbers:
        return []
    # return [numbers[i:i + size] for i in range(0, len(numbers), size)]
    return [numbers[:size]] + chunk(numbers[size:], size)


print(chunk([1, 2, 3, 4, 5], 2))
