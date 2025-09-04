def two_sum(nums: list[int], target: int) -> list[int]:
    num_dict: dict[int, int] = {}
    for i, num in enumerate(nums):
        num_dict[num] = i
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in num_dict and i != num_dict[num2]:
            return [i, num_dict[num2]]
    return []


def main():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    assert two_sum([0, 3, -3, 4, -1], -1) == [0, 4]


if __name__ == "__main__":
    main()