# 11004

num, index = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))


# 정렬해서 index 번째 수를 출력하면 된다.
# 단, index는 1부터 시작한다.

print(sorted(num_list)[index-1])