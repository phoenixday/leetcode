def set_zeroes(matrix: list[list[int]]) -> None:
    is_zero_col = False
    for i, row in enumerate(matrix):
        if matrix[i][0] == 0:
            is_zero_col = True
        for j, col in enumerate(row):
            if j > 0 and col == 0:
                matrix[i][0], matrix[0][j] = 0, 0
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i > 0 and j > 0  and (matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j, _ in enumerate(matrix[0]):
            matrix[0][j] = 0
    if is_zero_col:
        for i, _ in enumerate(matrix):
            matrix[i][0] = 0
    return


def main():
    tests = [
        [[1,1,1],[1,0,1],[1,1,1]],
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
        [[-1],[2],[3]],
        [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    ]
    expected = [
        [[1,0,1],[0,0,0],[1,0,1]],
        [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
        [[-1],[2],[3]],
        [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    ]
    for test, expected in zip(tests, expected):
        set_zeroes(test)
        assert test == expected

if __name__ == "__main__":
    main()
