def check_palindrome(s):
    clean_chars = []
    for char in s:
        if char.isalpha() or char.isdigit():
            clean_chars.append(char.lower())

    clean_str = ''.join(clean_chars)

    length = len(clean_str)
    for i in range(length // 2):
        if clean_str[i] != clean_str[length - 1 - i]:
            return False

    return True

if __name__ == "__main__":
    examples = [
        "Cigar? Toss it in a can. It is so tragic.",
        "Кот-ток",
        "1234554321",
        "Я рахит, воняю я, но втихаря",
        "Hello!"
    ]

    for example in examples:
        res = check_palindrome(example)
        print(f"Строка '{example}' - это палиндром: {res}")
