from typing import Dict, List, Tuple, Optional

# Define types using type aliases
Board = Dict[int, str]
WinningCombination = Tuple[int, int, int]

# Winning combinations
win_combo: List[WinningCombination] = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 5, 9),
    (7, 5, 3),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
]

# Game board
board: Board = {
    1: "X",
    2: "X",
    3: "X",
    4: "O",
    5: "O",
    6: "X",
    7: "X",
    8: "O",
    9: "O",
}


def is_winning_combo(
    board: Board, symbol: str
) -> Tuple[bool, Optional[WinningCombination]]:
    if len(symbol) != 1:
        raise ValueError("Symbol must be a single character")

    for combo in win_combo:
        if all(board[x] == symbol for x in combo):
            return True, combo
    return False, None


# Test the function
print(is_winning_combo(board, "X"))  # (True, (1, 2, 3))
