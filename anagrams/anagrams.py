def reverse_word(word):
    reversed_word = []

    letters = [letter for letter in word if letter.isalpha()]

    for letter in word:
        if letter.isalpha():
            reversed_word.append(letters.pop())
        else:
            reversed_word.append(letter)
    result = ''.join(reversed_word)
    return result


def reverse_string(string):
    reversed_string = []

    for char in string.split(' '):
        reversed_string.append(reverse_word(char))
    result = ' '.join(reversed_string)
    return result


if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]
    for text, reversed_text in cases:
        assert reverse_string(text) == reversed_text
