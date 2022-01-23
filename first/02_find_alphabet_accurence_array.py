def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for s in string:
        if s.isalpha() :
            alphabet_occurrence_array[ord(s)-97] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
