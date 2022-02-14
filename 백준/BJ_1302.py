from collections import Counter

n = int(input())
i_list = list()
for _ in range(n):
    a = input()
    i_list.append(a)

l_count = Counter(i_list).most_common()
sorted_list = sorted(l_count, key=lambda item: (-item[1], item[0]))
print(sorted_list.pop(0)[0])
