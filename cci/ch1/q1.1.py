def is_unique(letters):
    letters = ''.join(sorted(letters))

    for i in range(len(letters) - 1):
        if letters[i] == letters[i + 1]:
            return False

    return True


if __name__ == "__main__":
    assert is_unique("paulo")
    assert is_unique("")
    assert not is_unique("paulop")
    assert not is_unique("google")
