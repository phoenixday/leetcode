def trap(height: list[str]) -> int:
    res, left, right, left_max, right_max = 0, 0, len(height) - 1, 0, 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            res += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            res += right_max - height[right]
            right -= 1
    return res


def main():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0] * 20000) == 0


if __name__ == "__main__":
    main()
