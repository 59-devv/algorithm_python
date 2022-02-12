"""
1. BFS, DFS
    # 너비 우선 탐색 (Breadth First Search)
    # 깊이 우선 탐색 (Depth First Search)
    * BFS : 정점들과 같은 레벨에 있는 노드 (형제)를 먼저 탐색하는 방식
    * DFS : 정점의 자식들을 먼저 탐색하는 방식

2. 파이썬으로 그래프 표현하는 방법
    * Key/Value 형태의 Dictionary와 List를 활용
    * Key = 본인, Value = (List)연결된 모든 노드

3. BFS 구현
    * need_visit queue : 방문이 필요한 노드
    * visited queue : 이미 방문한 노드
    (1) 시작 노드의 key 값을 need_visit에 저장
    (2) (1)을 꺼내고, visited에 있는지 확인 후 없을 경우에 visited에 저장하면서, 시작 노드의 dictionary에 담긴 value들을 need_visit에 저장
        * 없을 경우 아무것도 안하고 다음 값으로 넘어감
    (3) 이 것을 계속 반복함

4. 시간 복잡도
    * 노드 수: V
    * 간선 수: E
    * 시간 복잡도 = O(V+E)

"""
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


# 3. BFS 구현
def bfs(gr, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while len(need_visit) != 0:
        data = need_visit.pop(0)
        if data not in visited:
            visited.append(data)
            need_visit.extend(gr[data])

    return visited


print(bfs(graph, 'A'))