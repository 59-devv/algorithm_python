input = "hello my name is 스파르타"


def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26
    max_num = alphabet_array[0]
    for s in string:
        if s.isalpha():
            alphabet_array[ord(s)-97] += 1

    for num in alphabet_array:
        if num > max_num:
            max_num = num

    max_alphabet_index = alphabet_array.index(max_num)

    return chr(max_alphabet_index + 97)


result = find_max_occurred_alphabet(input)
print(result)