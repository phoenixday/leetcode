# reverse over main diagonal
def transpose(matrix: list[list[int]]) -> None:
    for i, row in enumerate(matrix):
        for j in range(i, len(row)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# reverse from left to right
def reflect(matrix: list[list[int]]) -> None:
    for i, row in enumerate(matrix):
        for j in range(len(row) // 2):
            end = len(row) - 1
            matrix[i][j], matrix[i][end - j] = matrix[i][end - j], matrix[i][j]


def rotate(matrix: list[list[int]]) -> None:
    transpose(matrix)
    reflect(matrix)


def main():
    tests = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
        [[1]],
        [[1,2], [4,3]]
    ]
    expected = [
        [[7,4,1],[8,5,2],[9,6,3]],
        [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
        [[1]],
        [[4,1],[3,2]]
    ]
    for test, expected in zip(tests, expected):
        rotate(test)
        assert test == expected

if __name__ == "__main__":
    main()
