# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때
# (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
#472 385


data = input()

a = data.split()[0]
b = data.split()[1]

for i in range(len(a)):
    print(int(b[len(b)-1-i]) * int(a))
    if i == len(a)-1:
        print(int(a)*int(b))
