def truncate_string(source: str, size: int) -> str:
    if not source:
        raise ValueError("Source must be a valid string")
    if size < 0:
        raise ValueError("Size must be a positive integer")

    # return (
    #     source[: size - 3 if size > 3 else size] + "..."
    #     if len(source) != size
    #     else source
    # )

    if len(source) == size:
        return source

    truncate_point = size - 3 if size > 3 else size
    return f"{source[:truncate_point]}..."


print(
    truncate_string(
        "A-tisket, a-tasket A green and yellow basket",
        len("A-tisket, a-tasket A green and yellow basket"),
    )
)
# A-tisket, a-tasket A green and yellow basket
print(truncate_string("A-tisket, a-tasket A green and yellow basket", 11))
# A-tisket...
print(truncate_string("A-tisket...", 1))
# A...
