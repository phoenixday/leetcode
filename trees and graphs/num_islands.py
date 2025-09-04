import collections

def visit(grid: list[list[str]], start_i: int, start_j: int):
    queue = collections.deque([(start_i, start_j)])
    while queue:
        i, j = queue.popleft()
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "x"
            queue.append((i, j + 1))
            queue.append((i + 1, j))
            queue.append((i, j - 1))
            queue.append((i - 1, j))


def num_islands(grid: list[list[str]]) -> int:
    num = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "1":
                num += 1
                visit(grid, i, j)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "x":
                grid[i][j] = "1"
    return num


def main():
    tests = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    ]
    expected = [
        1,
        3
    ]
    for test, expected in zip(tests, expected):
        assert num_islands(test) == expected


if __name__ == "__main__":
    main()
