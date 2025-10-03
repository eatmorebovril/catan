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
