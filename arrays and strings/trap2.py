def trap(height: list[str]) -> int:
    max_left, max_right = [0] * len(height), [0] * len(height)
    max_left[0], max_right[-1] = height[0], height[-1]
    for i in range(1, len(max_left)):
        max_left[i] = max(height[i], max_left[i - 1])
    for i in range(len(max_right) - 2, -1, -1):
        max_right[i] = max(height[i], max_right[i + 1])
    res = sum(min(max_left[i], max_right[i]) - height[i] for i in range(len(height)))
    return res


def main():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0] * 20000) == 0


if __name__ == "__main__":
    main()