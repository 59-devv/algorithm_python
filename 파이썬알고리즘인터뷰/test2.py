s2 = [1, 2, 3]
s = [3, -1, 0, 4]
cnt = 0
stack = []

for i in range(len(s)):
    if i == 0:
        if s[i] > s[i+1]:
            stack.append(s[i]-1)
            stack.append(s[i])
            cnt += 1
        else:
            stack.append(s[i])
    else:
        if len(stack) == 1:
            if stack[0] > s[i]:
                stack.append(s[i]-1)
                stack.append(s[i])
                cnt += 1
                print(cnt)
            else:
                stack.append(s[i])

        else:
            if stack[-2] > stack[-1]:
                if stack[-1] > s[i]:
                    stack.append(stack[-1]+1)
                    stack.append(s[i])
                    cnt += 1
                    print(cnt)
                else:
                    stack.append(s[i])
            else:
                if stack[-1] > s[i]:
                    stack.append(s[i])
                else:
                    if stack[-1]-1 in stack:
                        stack.append(stack[-1]-2)
                        stack.append(s[i])
                        cnt += 1
                    else:
                        stack.append(stack[-1]-1)
                        stack.append(s[i])
                        cnt += 1


print(cnt)