import collections

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = collections.defaultdict(list)
    for s in strs:
        ss = "".join(sorted(s))
        groups[ss].append(s)
    return list(groups.values())


def main():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]


if __name__ == "__main__":
    main()