RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)

def add(point: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    return (point[0] + direction[0], point[1] + direction[1])

def turn_right(curr_direction: tuple[int, int]) -> tuple[int, int]:
    directions = [RIGHT, DOWN, LEFT, UP]
    for i, direction in enumerate(directions):
        if direction == curr_direction:
            return directions[(i + 1) % 4]
    return RIGHT


def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []
    direction = RIGHT
    i, j = 0, 0
    while matrix[i][j] != 101:
        res.append(matrix[i][j])
        matrix[i][j] = 101
        next_i, next_j = add((i, j), direction)
        s = 0
        while (not (0 <= next_i < len(matrix)) \
            or not (0 <= next_j < len(matrix[0])) \
                or matrix[next_i][next_j] == 101) and s < 4:
            direction = turn_right(direction)
            next_i, next_j = add((i, j), direction)
            s += 1
        if s == 4:
            break
        i, j = next_i, next_j
    return res



def main():
    tests = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [[1]]
    ]
    expected = [
        [1,2,3,6,9,8,7,4,5],
        [1,2,3,4,8,12,11,10,9,5,6,7],
        [1]
    ]
    for test, expected in zip(tests, expected):
        assert spiral_order(test) == expected

if __name__ == "__main__":
    main()
