"""
1. 그래프란?
    : 실제 세계의 현상이나 사물을 정점(Vertex) 또는 노드(Node)와 간선(Edge)으로 표현

2. 그래프 관련 용어
    * 노드(Node) : 위치를 말함 == 정점(Vertex)
    * 간선(Edge) : 위치간의 관계를 표시한 선 (노드와 노드 연결). 링크라고도 함
    * 인접 정점 (Adjacent Vertex) : 간선으로 직접 연결된 노드
    * 참고 용어
        # 정점의 차수(Degree) : 무방향 그래프에서 하나의 정점에 인접한 정점 수
        # 진입 차수(In-Degree) : 방향 그래프에서 외부로부터 들어온 간선 수
        # 진출 차수(Out-Degree) :  방향 그래프에서 내부로부터 나간 간선 수
        # 경로 길이(Path Length) : 경로를 구성하기 위해 사용된 간선 수
        # 단순 경로(Simple Path) : 처음 정점과 끝 정점을 제외하고, 중복된 정점이 없는 경로
        # 사이클(Cycle) : 단순 경로의 시작 정점과 종료 정점이 동일한 경우

3. 그래프의 종류
    (1) 무방향 그래프
        * 방향이 없는 그래프
        * 간선을 통해 노드는 양방향으로 갈 수 있음
        * 보통 노드 A,B가 연결되어 있을 경우 (A,B) 또는 (B, A)로 표기

    (2) 방향 그래프
        * 간선에 방향이 있는 그래프
        * 보통 노드 A,B가 A->B로 가는 간선으로 연결되어있을 경우, <A,B>로 표기
        * <B,A>는 <A,B> 와 방향이 다르기 때문에 전혀 다른 표기임

    (3) 가중치 그래프 (잘 쓰임)
        * 간선에 비용 또는 가중치가 할당된 그래프
        * 최적화된 경로를 판단하는데 비용을 활용하여 계산함

    (4) 연결 그래프와 비연결 그래프
        * 연결그래프 : 무방향 그래프에 있는 모든 노드에 대해, 항상 경로가 존재하는 경우
        * 비연결그래프 : 무방향 그래프에서 특정 노드에 대해 경로가 존재하지 않는 경우

    (5) 사이클과 비순환 그래프
        * 사이클 : 단순 경로의 시작 노드와 종료 노드가 동일한 경우
        * 비순환그래프 : 사이클이 없는 그래프

    (6) 완전 그래프
        : 그래프의 모든 노드가 서로 연결되어 있는 그래프

4. 그래프와 트리의 차이
    * 트리는 그래프에 속하는 특별한 종류라고 할 수 있다.
    (1) 정의
        * 그래프 : 노드와 노드를 연결하는 간선으로 표현되는 자료 구조
        * 트리 : 그래프의 한 종류. 방향성이 있는 비순환 그래프
    (2) 방향성
        * 그래프 : 방향 그래프, 무방향 그래프 둘 다 존재
        * 트리 : 방향 그래프만 존재
    (3) 사이클
        * 그래프 : 사이클 가능함. 순환 및 비순환 그래프 모두 존재
        * 트리 : 비수노한 그래프로 사이클이 존재하지 않는다.
    (4) 루트 노드
        * 그래프 : 루트 노드 존재하지 않는다.
        * 트리 : 루트 노드를 정해놓고 시작하는 것이 일반적임
    (5) 부모/자식 관계
        * 그래프 : 기본적으로 존재하지 않음
        * 트리 : 기본적으로 부모/자식 관계가 존재함

"""