def merge(lst1: list[int], lst2: list[int]) -> list[int]:
    i, j = 0, 0
    res = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            res.append(lst2[j])
            j += 1
        else:
            res.append(lst1[i])
            i += 1
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    while j < len(lst2):
        res.append(lst2[j])
        j += 1
    return res


def merge_sort(nums: list[int], start: int, end: int) -> list[int]:
    if start == end:
        return [nums[start]]
    mid = start + (end - start) // 2
    lst1 = merge_sort(nums, start, mid)
    lst2 = merge_sort(nums, mid + 1, end)
    return merge(lst1, lst2)


# hoare
def quicksort(nums: list[int], start: int, end: int):
    if start >= end:
        return
    mid = start + (end - start) // 2
    pivot = nums[mid]
    i, j = start, end
    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    quicksort(nums, start, j) # j will be less than i at the end
    quicksort(nums, i, end)


def main():
    tests = [
        [3, 2, 4, 7, 1],
        [4, 4, 2, 2, 8, 4],
        [3, 4, 1, 1, 9],
        [4, 4, 4, 4, 4],
        [2, 2, 1, 2, 2, 3],
        [1],
        [2, 1],
        [1, 2]
    ]
    for t in tests:
        # assert merge_sort(t, 0, len(t) - 1) == sorted(t)
        quicksort(t, 0, len(t) - 1)
        assert t == sorted(t)


if __name__ == "__main__":
    main()
