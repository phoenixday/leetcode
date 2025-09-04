def is_palindrome(s: str) -> bool:
    # s = "".join(c.lower() if c.isalnum() else "" for c in s)
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def main():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True


if __name__ == "__main__":
    main()
