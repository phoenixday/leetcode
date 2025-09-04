def trap(height: list[str]) -> int:
    i, res = 0, 0
    minn = min(height)
    height = [h - minn for h in height]
    while i + 1 < len(height):
        print("i: ", i)
        if height[i] < height[i + 1]:
            i += 1
            continue
        max_height, end = height[i + 1], i + 1
        for j in range(i + 1, len(height)):
            print("j: ", j)
            if max_height < height[j]:
                max_height, end = min(height[i], height[j]), j
            if max_height >= height[i]:
                break
        res += sum(max_height - height[i] for i in range(i + 1, end))
        i = end
    return res


def main():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    # assert trap([4,2,0,3,2,5]) == 9
    # assert trap([0] * 20000) == 0


if __name__ == "__main__":
    main()