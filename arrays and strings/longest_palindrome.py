def is_palindrome(s: str, s1: int, s2: int) -> bool:
    i, j = s1, s2
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longest_palindrome(s: str) -> str:
    i, length = 0, len(s)
    while length > 1:
        if is_palindrome(s, i, i + length - 1):
            break
        if i + length < len(s):
            i += 1
        else:
            length -= 1
            i = 0
    return s[i : i + length]


def main():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("abc") in ["a", "b", "c"]
    assert longest_palindrome('e' * 1000) == 'e' * 1000


if __name__ == "__main__":
    main()
