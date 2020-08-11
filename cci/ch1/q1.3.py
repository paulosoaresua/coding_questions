def urlify(letters, length):
    letters = list(letters)

    offset = 0
    for i in range(length):
        if letters[i] == " ":
            offset += 2

    if offset != 0:
        for i in range(length-1, -1, -1):
            if letters[i] == " ":
                letters[i + offset] = '0'
                letters[i + offset - 1] = '2'
                letters[i + offset - 2] = '%'
                offset -= 2
            else:
                letters[i + offset] = letters[i]

    return ''.join(letters)


if __name__ == "__main__":
    assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert urlify("", 0) == ""
    assert urlify("            ", 4) == "%20%20%20%20"
    assert urlify("Mr John  Smith      ", 14) == "Mr%20John%20%20Smith"
