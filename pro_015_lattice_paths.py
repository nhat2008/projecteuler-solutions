# problem 15


def get_triangle(n):
    x = [[1]]
    for i in range(n - 1):
        x.append([sum(i) for i in zip([0] + x[-1], x[-1] + [0])])
    return x


def run():
    rows = 20
    columns = 20
    triangle = get_triangle(2 * rows + 1)
    return triangle[2 * rows][columns]


print run()