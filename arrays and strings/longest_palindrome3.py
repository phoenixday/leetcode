# considering s[s1] == s[s2]
def palindrome(s: str, s1: int, s2: int) -> tuple[int, int]:
    if s[s1] != s[s2]:
        return s1, s2
    i, j = s1, s2
    while 0 <= i and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return i + 1, j - 1


def longest_palindrome(s: str) -> str:
    ans_start, ans_end = 0, 0
    for i, ss in enumerate(s):
        for l in [0, 1]:
            if i + l < len(s) and ss == s[i + l]:
                start, end = palindrome(s, i, i + l)
                if ans_end - ans_start < end - start:
                    ans_start, ans_end = start, end
    return s[ans_start: ans_end + 1]


def main():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("abc") in ["a", "b", "c"]
    assert longest_palindrome("bb") == "bb"
    assert longest_palindrome('e' * 1000) == 'e' * 1000


if __name__ == "__main__":
    main()
