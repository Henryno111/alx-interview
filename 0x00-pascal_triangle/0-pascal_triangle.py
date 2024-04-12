#!/usr/bin/python3
def pascal_triangle(n):

    if n <= 0:
        return []:
            triangle = []

    # Create the first row with a single 1
    triangle.append([1])

    # Iterate through rows from 1 to n-1 (excluding the first row)
    for i in range(1, n):
        row = []

    # The first element in each row is always 1
    row.append(1)

    for j in range(1, i):
        previous_row = triangle[i-1]
    element = previous_row[j] + previous_row[j-1]
    row.append(element)

    # The last element in each row is always 1
    row.append(1)

    # Append the completed row to the triangle
    triangle.append(row)

    return triangle

    # Example usage (uncomment to print the triangle)
    # print(pascal_triangle(6))
