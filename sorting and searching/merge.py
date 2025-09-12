def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    i, j, last = m - 1, n - 1, len(nums1) - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1


def main():
    tests = [
        ([1, 2, 3, 5, 6, 8, 0, 0, 0], 6, [2, 5, 6], 3),
        ([1,2,3,0,0,0], 3, [2,5,6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
        ([4,5,6,0,0,0], 3, [1,2,3], 3)
    ]
    expected = [
        [1, 2, 2, 3, 5, 5, 6, 6, 8],
        [1,2,2,3,5,6],
        [1],
        [1],
        [1,2,3,4,5,6]
    ]
    for test, expected in zip(tests, expected):
        nums1, m, nums2, n = test
        merge(nums1, m, nums2, n)
        assert nums1 == expected

if __name__ == "__main__":
    main()
