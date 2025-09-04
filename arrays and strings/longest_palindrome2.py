def longest_palindrome(s: str) -> str:
    memory = [[False] * len(s) for _ in range(len(s))]
    start, end = 0, 0
    length = 0
    while length < len(s):
        for i in range(len(s) - length):
            if length == 0:
                memory[i][i] = True
            if length == 1:
                memory[i][i + 1] = s[i] == s[i + 1]
            if length > 1:
                memory[i][i + length] = s[i] == s[i + length] and memory[i + 1][i + length - 1]
            if memory[i][i + length]:
                start, end = i, i + length
        length += 1
    return s[start : end + 1]


def main():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("abc") in ["a", "b", "c"]
    assert longest_palindrome('e' * 1000) == 'e' * 1000


if __name__ == "__main__":
    main()
