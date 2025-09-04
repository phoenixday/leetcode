# runtime: 3 ms
# memory usage: 18.6 MB

def two_sum(nums: list[int], target: int) -> list[int]:
    if target < 0:
        for i, num in enumerate(nums):
            nums[i] = -num
        target = -target
    sorted_nums = sorted(nums)
    # last_i = len(sorted_nums) - 1
    # for i, num in enumerate(sorted_nums):
    #     if num > target:
    #         last_i = i - 1
    first_sorted_i = 0
    last_sorted_i = modified_binary_search(sorted_nums, target)
    while sorted_nums[first_sorted_i] + sorted_nums[last_sorted_i] != target:
        if sorted_nums[first_sorted_i] + sorted_nums[last_sorted_i] > target:
            last_sorted_i -= 1
        elif sorted_nums[first_sorted_i] + sorted_nums[last_sorted_i] < target:
            first_sorted_i += 1
    first_i, last_i = -1, -1
    for i, num in enumerate(nums):
        if first_i != -1 and last_i != -1:
            break
        if first_i == -1 and num == sorted_nums[first_sorted_i]:
            first_i = i
        elif last_i == -1 and num == sorted_nums[last_sorted_i]:
            last_i = i
    return [first_i, last_i]
        

def modified_binary_search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            if mid > 0 and nums[mid - 1] < target:
                return mid - 1
            end = mid - 1
        elif nums[mid] < target:
            if (mid < len(nums) - 1 and nums[mid + 1] > target) or mid == len(nums) - 1:
                return mid
            start = mid + 1
    return -1


def main():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    assert two_sum([0, 3, -3, 4, -1], -1) == [0, 4]
    nums = {
        1: [1, 3, 3, 5],
        2: [5, 4, 7]
    }
    print(nums[2])
    nums[3] = [5, 4]
    print(nums[3])


if __name__ == "__main__":
    main()