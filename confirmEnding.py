def confirm_ending(target: str, suffix: str) -> bool:
    # Handle empty strings
    if not suffix and not target:
        return True

    return target.endswith(suffix)


print(confirm_ending("Ricardo Manuel", "Manuelx"))
