BUTTONS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letter_combinations(digits: str, i=0) -> list[str]:
    if i == len(digits):
        return []
    res = []
    endings = letter_combinations(digits, i + 1)
    for letter in BUTTONS[digits[i]]:
        if len(endings) > 0:
            for ending in endings:
                res.append(letter + ending)
        else:
            res.append(letter)
    return res


def main():
    tests = [
        "23",
        "",
        "2",
        "7"
    ]
    expected = [
        ["ad","ae","af","bd","be","bf","cd","ce","cf"],
        [],
        ["a","b","c"],
        ["p","q","r","s"]
    ]
    for test, expected in zip(tests, expected):
        assert letter_combinations(test) == expected

if __name__ == "__main__":
    main()
