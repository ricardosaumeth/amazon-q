from typing import List


def get_index_to_ins(numbers: List[float], target: float) -> int:
    if not isinstance(numbers, List):
        raise ValueError("Input must be valid integers")
    if not isinstance(target, (int, float)):
        raise ValueError("target must be a valid number")

    try:
        return next(index for index, value in enumerate(numbers) if value >= target)
    except StopIteration:
        return len(numbers)


print(get_index_to_ins([1, 2, 3, 4], 2.5))  # 1
