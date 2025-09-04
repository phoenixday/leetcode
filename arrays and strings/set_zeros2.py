def set_zeroes(matrix: list[list[int]]) -> None:
    zero_rows, zero_cols = set(), set()
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i in zero_rows or j in zero_cols:
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
