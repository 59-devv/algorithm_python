# 애너그램이란?
# 일종의 언어유희로, 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.

# 문자열 배열을 받아 애너그램 단위로 그룹핑하시오.

# 입력
import collections

anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 출력
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]

# 가장 간단하게 애너그램인지 판단하는 방법은, 정렬해서 비교하는 것이다.
# 즉, 정렬했을 때 똑같은지를 확인하면 된다.

def group_anagrams(strs):
    # key : value 형태로 저장하기 위해 dictionary를 사용하는데,
    # 기본 dict는 해당 key가 존재하지 않으면 KeyError를 발생시키므로
    # key가 없으면 자동으로 생성하면서 값을 넣어주는 defaultdict를 사용한다.
    a = collections.defaultdict(list)

    for word in strs:
        a[''.join(sorted(word))].append(word)

    return a.values()

print(group_anagrams(anagrams))
