def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    counting_table = {}

    for s in string1:
        if s in counting_table.keys():
            counting_table[s] += 1
        else:
            counting_table[s] = 1

    for s in string2:
        if s not in counting_table.keys():
            return False
        elif counting_table[s] == 0:
            return False
        else:
            counting_table[s] -= 1

    return True


if __name__ == "__main__":
    assert is_permutation("paulo", "oluap")
    assert is_permutation("", "")
    assert is_permutation("paulo", "pulao")
    assert not is_permutation("paulo", "ricardo")
    assert not is_permutation("paulo", "oular")
