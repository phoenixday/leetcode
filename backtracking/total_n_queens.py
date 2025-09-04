#   0 1 2 3 4
# 0 _ _ _ _ _
# 1 x _ _ _ _
# 2 _ x _ _ _
# 3 _ _ x _ _
# 4 _ _ _ x _

#   0 1 2 3 4
# 0 _ x _ _ _
# 1 _ _ x _ _
# 2 _ _ _ x _
# 3 _ _ _ _ x
# 4 _ _ _ _ _

#   0 1 2 3 4
# 0 _ _ _ x _
# 1 _ _ x _ _
# 2 _ x _ _ _
# 3 x _ _ _ _
# 4 _ _ _ _ _

#   0 1 2 3 4
# 0 _ _ _ _ _
# 1 _ _ _ _ x
# 2 _ _ _ x _
# 3 _ _ x _ _
# 4 _ x _ _ _



def total_n_queens(n: int) -> int:

    def backtrack(row: int, cols: set[int], diags: set[int], anti_diags: set[int]) -> int:
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if col not in cols and row - col not in diags and row + col not in anti_diags:
                cols.add(col)
                diags.add(row - col)
                anti_diags.add(row + col)
                count += backtrack(row + 1, cols, diags, anti_diags)
                cols.remove(col)
                diags.remove(row - col)
                anti_diags.remove(row + col)
        return count

    return backtrack(0, set(), set(), set())


def main():
    tests = [ 4, 1, 7 ]
    expected = [ 2, 1, 40 ]
    for test, expected in zip(tests, expected):
        assert total_n_queens(test) == expected


if __name__ == "__main__":
    main()
