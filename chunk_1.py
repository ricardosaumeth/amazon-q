def chunk(numbers: list[float], size: int) -> list[list[float]]:
    if not numbers:
        return []
    if len(numbers) and size:
        return [numbers[:size]] + chunk(numbers[size:], size)
    else:
        raise ValueError("Numbers and size must be valid inputs")


print(chunk([1, 2, 3, 4, 5], 2))
