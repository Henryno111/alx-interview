def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle
    up to the nth row.
    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row [1]

    for row in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        current_row = [1]  # Each row starts and ends with 1

        # Calculate the middle values
        for i in range(1, row):
            value = prev_row[i - 1] + prev_row[i]
            current_row.append(value)

        current_row.append(1)  # Add the final 1 for the row
        triangle.append(current_row)

    return triangle
