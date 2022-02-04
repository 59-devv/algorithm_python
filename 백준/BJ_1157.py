import collections
import sys

word = sys.stdin.readline().upper()


def find_most_frequent_number(word: str) -> str:
    word_list = list(word)

    # 방법1. count() 함수 사용하기
    # word_dict = {}
    # for w in word_list:
    #     word_dict[w] = word_list.count(w)
    #
    # result_list = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    #
    # return result_list[0][0] \
    #     if result_list[0][1] != result_list[1][1] else "?"
    #
    # 방법2. collections.Counter 사용하기
    result_list = collections.Counter(word_list[:-1])
    reversed_result = sorted(result_list.items(), key=lambda item: item[1], reverse=True)

    return reversed_result[0][0] \
        if reversed_result[0][1] != reversed_result[1][1] else "?"


print(find_most_frequent_number(word))