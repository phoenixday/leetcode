def reverse_string(s: list[str]) -> None:
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def main():
    tests = [
        ["h","e","l","l","o"],
        ["H","a","n","n","a","h"]
    ]
    expected = [
        ["o","l","l","e","h"],
        ["h","a","n","n","a","H"]
    ]
    for test, expected in zip(tests, expected):
        reverse_string(test)
        assert test == expected


if __name__ == "__main__":
    main()
