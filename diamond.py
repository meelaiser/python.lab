def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    mid = height // 2
    lines = []
    for l in height:
        if l + 1 < mid:
            lines[1] = " " * (mid - (l + 1)) + "/" * (1 + 1) + "\" * (1 + 1) + "\n""
    return "".join(lines)
    #pass
4 / 2
# diamond(4)
