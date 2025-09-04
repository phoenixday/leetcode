def reverse_words(s: str) -> str:
    ss = list(c for c in s)
    i, j = 0, 0
    while j < len(ss):
        while j < len(ss) and ss[j] == ' ':
            j += 1
        if j < len(ss) and i > 0:
            ss[i] = ' '
            i += 1
        w_start = i
        while j < len(ss) and ss[j] != ' ':
            ss[i] = ss[j]
            if i != j:
                ss[j] = ' '
            i += 1
            j += 1
        w_end = i - 1
        while w_start < w_end:
            ss[w_start], ss[w_end] = ss[w_end], ss[w_start]
            w_start += 1
            w_end -= 1
    i, j, s_end = 0, i - 1, i
    while i < j:
        ss[i], ss[j] = ss[j], ss[i]
        i += 1
        j -= 1
    return "".join(c for c in ss[:s_end])


def main():
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    assert reverse_words("a good   example") == "example good a"
    assert reverse_words("a") == "a"
    assert reverse_words("  an   ") == "an"


if __name__ == "__main__":
    main()
