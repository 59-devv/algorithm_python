import sys

loop_count = int(sys.stdin.readline())

for i in range(loop_count):
    data = sys.stdin.readline()

    temp_stack = []
    main_stack = []
    for d in data:
        if d == "<":
            if len(main_stack) > 0:
                temp_stack.append(main_stack.pop())
        elif d == ">":
            if len(temp_stack) > 0:
                main_stack.append(temp_stack.pop())
        elif d == "-":
            if len(main_stack) > 0:
                main_stack.pop()
        else:
            main_stack.append(d)

    print("".join(main_stack).replace("\n", "") + "".join(
        reversed(temp_stack)).replace("\n", ""))
