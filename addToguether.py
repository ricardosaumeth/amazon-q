def add_together(first: float):
    validate_number(first, "First")

    def inner(second: float) -> float:
        validate_number(second, "Second")
        return first + second

    return inner


def validate_number(number: float, position: str):
    if not isinstance(number, (int, float)) or isinstance(number, bool):
        raise ValueError(f"{position} must be  a valid number")


# Example usage
print(add_together(2)(30))  # Output: 32
# These will raise ValueError:
#add_together("not a number")(2)
# add_together(2)("not a number")
#add_together(True)(2)  # Boolean values are not allowed
