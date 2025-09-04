import collections

def trap(height: list[str]) -> int:
    res, stack = 0, collections.deque([])
    for i, curr_height in enumerate(height):
        while len(stack) > 0 and curr_height > height[stack[-1]]:
            deep_i = stack.pop()
            deep = height[deep_i]
            if len(stack) == 0:
                break
            res += (min(height[stack[-1]], curr_height) - deep) * (i - stack[-1] - 1)
        stack.append(i)
    return res


def main():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0] * 20000) == 0


if __name__ == "__main__":
    main()
