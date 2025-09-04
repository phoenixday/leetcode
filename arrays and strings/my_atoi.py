INT_MIN = pow(-2, 31) # -2147483648
INT_MAX = pow(2, 31) - 1 # 2147483647


def my_atoi(s: str) -> int:
    is_neg, number_started, res = False, False, 0
    for c in s:
        if c == " ":
            if number_started:
                break
        elif c in ["-", "+"] and not number_started:
            is_neg = c == "-"
            number_started = True
        elif c.isdigit():
            digit = ord(c) - ord('0')
            if res < 214748364:
                res = res * 10 + digit
            elif res == 214748364 and (digit <= 7 or (is_neg and digit <= 8)):
                res = res * 10 + digit
            else:
                return INT_MIN if is_neg else INT_MAX
            number_started = True
        else:
            break
    return res * -1 if is_neg else res

def main():
    assert my_atoi("42") == 42
    assert my_atoi(" -042") == -42
    assert my_atoi("1337c0d3") == 1337
    assert my_atoi("0-1") == 0
    assert my_atoi("words and 987") == 0
    assert my_atoi("   +0 123") == 0
    assert my_atoi("2147483649") == pow(2, 31) - 1
    assert my_atoi("-2147483649") == pow(-2, 31)
    assert my_atoi("-2147483648") == -2147483648
    assert my_atoi("-2147483647") == -2147483647
    assert my_atoi("21474836460") == 2147483647


if __name__ == "__main__":
    main()
