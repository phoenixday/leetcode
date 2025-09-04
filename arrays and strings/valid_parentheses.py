from collections import deque

def valid_parentheses(s: str) -> bool:
    p = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    d = deque()
    for c in s:
        if c in p:
            if len(d) == 0 or p[c] != d.pop():
                return False
        else:
            d.append(c)

    return len(d) == 0


def main():
    assert valid_parentheses("()") is True
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("(]") is False
    assert valid_parentheses("([])") is True
    assert valid_parentheses("([)]") is False


if __name__ == "__main__":
    main()
