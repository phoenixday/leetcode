# TODO not working

def solve_sudoku(board: list[list[str]]) -> None:

    def is_valid(num: str, i: int, j: int) -> bool:
        return not_in_row(num, i) \
            and not_in_col(num, j) \
                and not_in_box(num, i, j)


    def not_in_row(num: str, row: int):
        return not num in board[row]


    def not_in_col(num: str, col: int):
        for _, row in enumerate(board):
            if num == row[col]:
                return False
        return True


    def not_in_box(num: str, row: int, col: int):
        row_box, col_box = 3 * (row // 3), 3 * (col // 3)
        for i in range(row_box, row_box + 3):
            for j in range(col_box, col_box + 3):
                if num == board[i][j]:
                    return False
        return True

    def backtrack(i: int, j: int):
        while 0 <= i < len(board) and board[i][j] != '.':
            if j + 1 < len(board[0]):
                j += 1
            else:
                i, j = i + 1, 0

        if i >= len(board):
            return True

        for num in range(1, 10):
            if is_valid(str(num), i, j):
                board[i][j] = str(num)
                res = backtrack(i, j)
                if res:
                    return True
                board[i][j] = "."

        return False

    backtrack(0, 0)


def main():
    tests = [
        [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    ]
    expected = [
        [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
    ]
    for test, expected in zip(tests, expected):
        board = test
        solve_sudoku(board)
        assert board == expected

if __name__ == "__main__":
    main()
