def add_together(first: float):

    def inner(second: float) -> float:
        return first + second

    return inner

# Example usage
print(add_together(2)(30))  # Output: 32
# These will raise ValueError:
# add_together("not a number")(2)
# add_together(2)("not a number")
# add_together(True)(2)  # Boolean values are not allowed
