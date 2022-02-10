from collections import deque

board = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]]

c = 1

location: int = None
goal: int = None

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(len(board)):
    try:
        location = [i, board[i].index(2)]
        continue
    except:
        pass

    try:
        goal = [i, board[i].index(3)]
        continue
    except:
        pass


def break_rock(location, goal):
    cnt = 0
    x = location[0] - goal[0]
    y = location[1] - goal[1]
    current_x = location[0]
    current_y = location[1]
    if x != 0:
        if x > 0:
            for _ in range(abs(x)):
                current_x -= 1
                if board[current_x][current_y] == 1:
                    cnt += 1 + c
                else:
                    cnt += 1
        elif x < 0:
            for _ in range(abs(x)):
                current_x += 1
                if board[current_x][current_y] == 1:
                    cnt += 1 + c
                else:
                    cnt += 1
    if y != 0:
        if y > 0:
            for _ in range(abs(y)):
                current_y -= 1
                if board[current_x][current_y] == 1:
                    cnt += 1 + c
                else:
                    cnt += 1
        elif y < 0:
            for _ in range(abs(y)):
                current_y += 1
                if board[current_x][current_y] == 1:
                    cnt += (1 + c)
                else:
                    cnt += 1

    return cnt


def bfs(location, goal):
    board2 = board
    cnt = 0
    current_x = location[0]
    current_y = location[1]
    goal_x = goal[0]
    goal_y = goal[1]
    queue = deque()
    print(queue)
    queue.append((current_x, current_y))
    print(queue)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            if nx < 0 or ny < 0 or nx >= len(board2) or ny >= len(board2[0]):
                continue
            if board[nx][ny] == 1:
                continue
            if board[nx][ny] == 0:
                cnt += 1
    return cnt




# def avoid_rock():
#     cnt = 0
#     x = location[0] - goal[0]
#     y = location[1] - goal[1]
#     current_x = location[0]
#     current_y = location[1]
#
#     # go left
#     if x!= 0:
#         if x > 0:
#             while True:
#                 if board[current_x-1][current_y] == 0:
#                     current_x -= 1
#                     cnt += 1
#                 elif board[current_x-1][current_y] == 1:
#                     if current_y > 0 and board[current_x][current_y-1] == 0:
#                         current_y -= 1
#                         cnt += 1
#                     elif current_y > 0 and board[current_x][current_y-1] == 1:
#                         current_y += 1
#                         cnt += 1




print(break_rock())