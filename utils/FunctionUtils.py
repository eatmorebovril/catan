def snakeToCamelCase(snake_str: str) -> str:
    """
    Convert a snake_case string to CamelCase.

    Args:
        snake_str (str): The input string in snake_case format.

    Returns:
        str: The converted string in CamelCase format.
    """
    components = snake_str.split('_')
    if not components:
        return ''
    return components[0].lower() + ''.join(x.title() for x in components[1:])

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
