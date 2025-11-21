import math
from constants.constants import BOARD_HEIGHT
from customTypes.Board import SettlementPosition

def getRowLength(row_index: int) -> int:
    return 6 - abs(math.ceil((row_index - 6) / 2))

def inBoardRange(position: SettlementPosition) -> bool:
    """Check if a position is within board bounds."""
    row, col = position
    return (
            0 <= row < BOARD_HEIGHT and
            0 <= col < getRowLength(row)
    )

def rotateList(lst: list, offset: int) -> list:
    """
    Reorder a list by a given offset.

    Args:
        lst (list): The input list to be reordered.
        offset (int): The offset by which to reorder the list.

    Returns:
        list: The reordered list.
    """
    if not lst:
        return []

    offset = offset % len(lst) # Ensure offset is within bounds
    return lst[offset:] + lst[:offset]
