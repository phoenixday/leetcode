def swap(matrix: list[list[int]], i: int, j: int) -> None:
    end = len(matrix) - 1
    a_i, a_j = i, j # left up
    b_i, b_j = j, end - i # right up
    c_i, c_j = end - i, end - j # right down
    d_i, d_j = end - j, i # left down
    temp = matrix[a_i][a_j]
    matrix[a_i][a_j] = matrix[d_i][d_j]
    matrix[d_i][d_j] = matrix[c_i][c_j]
    matrix[c_i][c_j] = matrix[b_i][b_j]
    matrix[b_i][b_j] = temp


def rotate(matrix: list[list[int]]) -> None:
    i, end = 0, len(matrix)
    while i < end:
        for j in range(i, end - 1):
            swap(matrix, i, j)
        i += 1
        end -= 1


def main():
    tests = [
        [[1]],
        [[1,2], [4,3]],
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ]
    expected = [
        [[1]],
        [[4,1],[3,2]],
        [[7,4,1],[8,5,2],[9,6,3]],
        [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ]
    for test, expected in zip(tests, expected):
        rotate(test)
        assert test == expected

if __name__ == "__main__":
    main()
