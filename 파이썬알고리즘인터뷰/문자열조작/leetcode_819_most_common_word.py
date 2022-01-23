import collections

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분은 하지 않으며, 구두점(마침표, 쉽표) 또한 무시한다.
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 정규 표현식을 이용해서 구두점을 제거한 후 소문자로 바꾼다.
# 단, banned 리스트에 있는 단어는 제외한다.
replaced = [word for word in re.sub('[^\\w]', ' ', paragraph).lower().split()
         if word not in banned]

# collections.Counter를 이용해서 key:value 형태로 몇 번 사용되는지 확인하고,
# most_common 을 이용해서 가장 많이 사용되는 것 순서로 정렬시킨다.
# 그 후, 첫번째를 찾아서 key만 출력 한다.
print(collections.Counter(replaced).most_common()[0][0])
