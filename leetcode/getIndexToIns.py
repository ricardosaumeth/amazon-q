from typing import List


def get_index_to_ins(numbers: List[float], target: float) -> int:
    try:
        return next(index for index, value in enumerate(numbers) if value >= target)
    except StopIteration:
        return len(numbers)


print(get_index_to_ins([1, 2, 3, 4], 2.5))  # 1
