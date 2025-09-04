def reverse_words2(s: list[str]) -> None:
    i, j = 0, 0
    while j < len(s):
        while j < len(s) and s[j] == ' ':
            j += 1
        if j < len(s) and i > 0:
            s[i] = ' '
            i += 1
        w_start = i
        while j < len(s) and s[j] != ' ':
            s[i] = s[j]
            if i != j:
                s[j] = ' '
            i += 1
            j += 1
        w_end = i - 1
        while w_start < w_end:
            s[w_start], s[w_end] = s[w_end], s[w_start]
            w_start += 1
            w_end -= 1
    i, j = 0, i - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return


def main():
    tests = [
        ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],
        ["a"]
    ]
    expected = [
        ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"],
        ["a"]
    ]
    for test, expected in zip(tests, expected):
        reverse_words2(test)
        assert test == expected


if __name__ == "__main__":
    main()
