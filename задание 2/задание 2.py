def filter_strings(f, items):
    result = []
    for x in items:
        if f(x):
            result.append(x)
    return result

def main() -> None:
    data = ["apple", "banana", "a cat", "dog", "elephant", "ant", "bird"]

    filter_spaces = lambda s: ' ' not in s
    filter_letter_a = lambda s: s[0] != 'a' if s else True
    filter_lenght = lambda s: len(s) > 4

    r1 = filter_strings(filter_spaces, data)
    r2 = filter_strings(filter_letter_a, data)
    r3 = filter_strings(filter_lenght, data)

    print("Без пробелов:", r1)
    print("Не начинаются с 'a':", r2)
    print("Длина >= 5:", r3)

if __name__ == "__main__":
    main()
