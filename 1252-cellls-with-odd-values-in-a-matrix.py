from typing import List

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
    # shallow copy !? Huge difference where we put this statement
    # row = [0] * m
    matrix = []
    cells = 0
    for i in range(0,n):
        row = [0] * m
        matrix.append(row)
    for i in indices:
        r = i[0]; c = i[1]
        for x in range(0, m):
            matrix[r][x] += 1
        for y in range(0, n):
            matrix[y][c] += 1
    for row in matrix:
        for item in row:
            if item % 2 != 0:
                cells += 1


    print(matrix)
    return cells

print(oddCells(2, 3, [[0,1], [1,1]]))
