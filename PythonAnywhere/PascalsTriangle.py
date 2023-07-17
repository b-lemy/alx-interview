# #!/usr/bin/python3
# """
# contains the Pascal's Triangle function
# """


def pascal_triangle(n):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    triangle = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                n = 1
                row.append(n)
            else:
                n = triangle[i - 2][j - 1] + triangle[i - 2][j]
                row.append(n)
        triangle.append(row)

    return triangle


# pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
