# nums is sorted, and -1 is returned if no needle is found
def binary_search(nums: list[int], needle: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == needle:
            return mid
        if nums[mid] > needle:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def main():
    pass


if __name__ == "__main__":
    main()