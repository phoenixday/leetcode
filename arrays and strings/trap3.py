def trap(height: list[str]) -> int:
    res, temp, max_left_height = 0, 0, height[0]
    for h in height:
        if h < max_left_height:
            temp += max_left_height - h
        else:
            res += temp
            temp, max_left_height = 0, h
    if temp > 0:
        temp, max_right_height = 0, height[-1]
        for i in range(len(height) - 1, -1, -1):
            if max_right_height == max_left_height:
                break
            if height[i] < max_right_height:
                temp += max_right_height - height[i]
            else:
                res += temp
                temp, max_right_height = 0, height[i]
            i -= 1
    return res


def main():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0] * 20000) == 0


if __name__ == "__main__":
    main()
