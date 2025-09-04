def set_zeroes(matrix: list[list[int]]) -> None:
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 0:
                matrix[i][0] = 'x' if matrix[i][0] not in ['y', 'z'] else 'z'
                matrix[0][j] = 'y' if matrix[0][j] not in ['x', 'z'] else 'z'
    for i, _ in enumerate(matrix):
        if matrix[i][0] in ['x', 'z']:
            for j, _ in enumerate(matrix[0]):
                if matrix[i][j] not in ['y', 'z']:
                    matrix[i][j] = 0
    for j, _ in enumerate(matrix[0]):
        if matrix[0][j] in ['y', 'z']:
            for i, _ in enumerate(matrix):
                matrix[i][j] = 0
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
