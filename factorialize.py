def factorialize(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("Input must be a valid number")
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    #return 1 if number <= 1 else number * factorialize(number - 1)
    # Iterative implementation instead of recursive
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


print(factorialize(5))  # 120
print(factorialize(1))  # 1
print(factorialize(0))  # 1
#print(factorialize(-1))  # Input must be a non-negative integer
