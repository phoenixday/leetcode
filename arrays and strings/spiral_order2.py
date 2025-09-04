def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []
    start_row, start_col = 0, 0
    end_row, end_col = len(matrix), len(matrix[0])
    while start_row < end_row and start_col < end_col:
        # direction == RIGHT
        for j in range(start_col, end_col):
            res.append(matrix[start_row][j])
        start_row += 1
        # direction == DOWN:
        for i in range(start_row, end_row):
            res.append(matrix[i][end_col - 1])
        end_col -= 1
        if start_row == end_row or start_col == end_col:
            break
        # direction == LEFT:
        for j in range(end_col - 1, start_col - 1, -1):
            res.append(matrix[end_row - 1][j])
        end_row -= 1
        # direction == UP:
        for i in range(end_row - 1, start_row - 1, -1):
            res.append(matrix[i][start_col])
        start_col += 1
    return res


def main():
    tests = [
        [[2,5,8],[4,0,-1]],
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [[1]],
        [[1, 2]],
        [[1, 2, 3]],
        [[1], [2]],
        [[1], [2], [3]],
        [[1, 2], [4, 3]]
    ]
    expected = [
        [2,5,8,-1,0,4],
        [1,2,3,6,9,8,7,4,5],
        [1,2,3,4,8,12,11,10,9,5,6,7],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4]
    ]
    for test, expected in zip(tests, expected):
        assert spiral_order(test) == expected

if __name__ == "__main__":
    main()
