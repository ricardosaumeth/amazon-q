from typing import List, Optional


def chunk(numbers: List[float], size: int) -> Optional[float]:
    if not isinstance(numbers, List):
        raise ValueError("Numbers is not valid")
    if not isinstance(size, int) and size > 0:
        raise ValueError("Size must be a positive value")
    if not numbers:
        return []
    # return [numbers[i:i + size] for i in range(0, len(numbers), size)]
    return [numbers[:size]] + chunk(numbers[size:], size)


print(chunk([1, 2, 3, 4, 5], 2))
