import collections

def group_anagrams(strs: list[str]) -> list[list[str]]:
    counts = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        counts[tuple(count)].append(s)
    return list(counts.values())


def main():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]


if __name__ == "__main__":
    main()