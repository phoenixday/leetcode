def remove_duplicates(nums: list[int]) -> int:
    k = 1
    for i, num in enumerate(nums):
        if i > 0 and num <= nums[i - 1]:
            while k < len(nums) and nums[k] <= nums[i - 1]:
                k += 1
                if k == len(nums):
                    return i
            nums[i], nums[k] = nums[k], nums[i]
        if k > 1 and k >= len(nums) - 1:
            return i + 1
    return len(nums)


def remove_duplicates2(nums: list[int]) -> int:
    insert_i = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[insert_i] = nums[i]
            insert_i += 1
    return insert_i


def main():
    tests = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4],
        [1,2],
        [1,1],
        [1,2,3,4]
    ]
    expected = [
        [1,2],
        [0,1,2,3,4],
        [1,2],
        [1],
        [1,2,3,4]
    ]
    for test, expected in zip(tests, expected):
        k = remove_duplicates2(test)
        assert k == len(expected) and test[:k] == expected

if __name__ == "__main__":
    main()
