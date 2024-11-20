def confirm_ending(target: str, suffix: str) -> bool:
    # Input validation
    if not isinstance(target, str) or not isinstance(suffix, str):
        raise ValueError("Both inputs must be strings")

    # Handle empty strings
    if not suffix and not target:
        return True

    return target.endswith(suffix)


print(confirm_ending("Ricardo Manuel", "Manuelx"))
