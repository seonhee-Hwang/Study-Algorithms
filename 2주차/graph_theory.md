---
title: "기타 그래프 이론"
date: 2022-05-25T22:28:43+09:00
draft: false
type: post
---
#### [참고 원본 - 기타 그래프 이론](https://www.youtube.com/watch?v=aOhhNFTIeFI&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=8)

### Table of Contents
* 서로소 집합
    * [서로소 집합의 특징](#서로소-집합)
    * [서로소 집합의 구현](#서로소-집합-구현)
    * [서로소 집합의 활용](#서로소-집합-활용)
* 최소 신장 트리
    * [최소 신장 트리의 특징](#최소-신장-트리)
    * [크루스칼 알고리즘](#크루스칼-알고리즘)
* [위상 정렬](#위상-정렬)
* [리뷰](#리뷰)


### 서로소 집합
* 서로소 집합 $\rightarrow$ 공통 원소가 없는 두 집합을 의미 ({1, 2}, {3, 4} 두 집합은 공통 원소가 없으므로, 서로소 집합)
![서로소 집합](./graph_theory/서로소.png)
* 서로소 집합 자료 구조란?
    * 서로소 판별을 위해 사용할 수 있는 자료 구조
    * 서로소 부분 집합들로 나뉘어진 원소들의 데이터 처리를 위한 자료 구조
* 지원하는 연산
    * 합집합 연산 (Union) $\rightarrow$ 서로소 집합을 합치는 연산
    * 찾기 연산 (Find) $\rightarrow$ 특정한 원소가 속한 집합이 어디인지 알려주는 연산
    * Union 과 Find 연산을 지원하는 자료 구조로, Union-Find 자료 구조라고도 합니다.
* 서로소 집합 자료 구조에서 Root Node가 같은 원소는 같은 집합을 의미
---
### 서로소 집합 구현
* Tree 자료 구조 활용
* 주의 : Tree에서 Root Node는 최상단에 위치한 Node를 의미하며, 부모 Node는 각 Node 바로 위에 있는 Node를 의미한다.
* ex) 1 ~ 6을 가지는 서로소 집합 자료구조
    * 최초에는 1의 부모는 1, 2의 부모는 2와 같은 형식으로 자기 자신을 부모로 놓고 시작
    ![서로소집합_최초상태](./graph_theory/최초상태.png)
    * 합치기 연산
        * Union(A, B) $\rightarrow$ A의 Root인 A'과 B의 Root인 B'을 찾아서, 내부적인 규칙(작은 값 or 큰 값이 높은 우선 순위)에 맞춰서 A'의 부모를 B'의 부모로 설정
        * ex) Union(0, 3) $\rightarrow$ 0의 Root인 0, 3의 Root인 3을 찾고, 0이 숫자가 작으므로, 3의 부모가 0이 되도록 변경
    * 이와 같은 합치기 연산을 통해, 합치기를 진행
    * Union(1, 4), Union(2, 3) 연산 진행 후의 결과
    ![서로소집합_합치기후](./graph_theory/합치기후.png)


* 단점 $\rightarrow$ 각 Node의 Root를 찾을 때, 한 번에 찾을 수 없고, 재귀를 통해, 자기의 부모가 자기 자신일 때까지 호출을 통해 찾을 수 있음
* ex) 5 $\rightarrow$ 4 $\rightarrow$ 3 $\rightarrow$ 2 $\rightarrow$ 1 의 형태로 된 구조라면, 5의 Root를 찾을 때까지 5번의 호출이 필요 
```python
def findRoot(parent, x): ## parent는 각 Node의 부모가 누구인지 적혀 있는 List, x는 부모를 찾을 Node
    if parent[x] != x:
        return findRoot(parent, parent[x])
    return x
```
* 경로 압축 알고리즘 $\rightarrow$ 위와 같은 비효율을 해결하기 위해, Find 함수를 재귀적으로 호출하면서, 모든 값의 부모를 Root로 Update
* 이런 방식을 사용하면, 최초 Root를 찾을 때를 제외하고는 시간 복잡도가 개선되는 장점이 있음!
```python
def findRoot(parent, x): ## parent는 각 Node의 부모가 누구인지 적혀 있는 List, x는 부모를 찾을 Node
    if parent[x] != x:
        parent[x] = findRoot(parent, parent[x])
    return parent[x]
```
---
### 서로소 집합 활용
* 무방향 그래프 내에서의 사이클 판별에 사용 (방향 그래프의 사이클 여부는 DFS를 통해 판별)
    1. 각 간선을 하나씩 확인하여, 연결된 두 Node의 Root Node를 확인
    2. 두 Node의 Root Node가 다르다면, 두 Node에 대해, 합집합 연산 수행
    3. 두 Node의 Root Node가 동일하다면, 사이클이 발생했다고 판단
    4. 그래프에 포함된 모든 간선에 대해 1 ~ 3의 과정을 반복
```python
def unionNode(parent, a, b): ## parent는 각 Node의 부모가 누구인지 적혀 있는 List, a, b는 합칠 Node
    root_a = findRoot(parent, a)
    root_b = findRoot(parent, b)
    if root_a < root_b: # 우선 순위에 따라 결정
        parent[b] = root_a
    else:
        parent[a] = root_b
```
```python
def findCycle(edges, parent): ## parent는 각 Node의 부모가 누구인지 적혀 있는 List, edges는 각 그래프의 Node 연결에 대한 정보가 있는 List
    for node_a, node_b in edges:
        root_a = findRoot(node_a)
        root_b = findRoot(node_b)
        if root_a == root_b:
            return True
        else:
            union(node_a, node_b)
    return False
```
---
### 최소 신장 트리
* 신장 트리 $\rightarrow$ 그래프에서 모든 Node를 포함하면서, 사이클이 없는 `부분 그래프`를 의미
    * Tree의 조건 $\rightarrow$ 모든 Node가 포함되어 연결되면서, 사이클이 존재하지 않음
* 최소 신장 트리 $\rightarrow$ 최소한의 비용으로 구성되는 신장 트리 (간선의 비용이 다를 경우)
* ex) 최소 비용으로 모든 도로를 연결하는 다리 만들기
* 최소 신장 트리의 간선 개수 $\rightarrow$ 전체 Node 수 - 1
![신장트리](./graph_theory/신장트리.png)

### 크루스칼 알고리즘
* 대표적인 최소 신장 트리 알고리즘 (그리디 알고리즘으로 분류)
* 크루스칼 알고리즘 구현
    1. 간선의 모든 비용을 오름차순으로 정렬
    2. 간선을 하나씩 확인하며, 사이클이 발생하는 지 확인
    3. 사이클이 발생하지 않는다면, 해당 간선을 최소 신장 트리에 포함
    4. 사이클이 발생한다면, 해당 간선을 포함하지 않고 다음으로
    5. 모든 간선에 대해 2 ~ 4의 과정을 반복
* 간선의 개수가 N개일 때, 시간 복잡도 $\rightarrow$ $O(NlogN)$
* 이는 가장 오래 걸리는 부분이, 전체 간선의 비용을 오름차순으로 정렬하는 것이기 때문
![크루스 칼알고리즘](./graph_theory/크루스칼알고리즘.png)

### 위상 정렬
* DAG (Directed Acyclic Graph) : 사이클이 없는 방향 그래프
* DAG의 모든 Node를 방향을 거스르지 않도록 순서대로 나열하는 것을 의미
* ex) 선수과목을 고려한 학습 순서 결정 문제
![선수과목](./graph_theory/선수과목.png)
* 위를 위상 정렬하면 `자료구조` $\rightarrow$ `알고리즘` $\rightarrow$ `고급 알고리즘`으로 정렬
* 방향 그래프의 진입차수 & 진출차수
    * 진입 차수 : 특정 Node로 들어오는 간선의 수
    * 진출 차수 : 특정 Node에서 나가는 간선의 수
![진입출차수](./graph_theory/진입출차수.png)
* 사이클이 있는 경우 사이클 내부에서는 진입 차수가 0이 될 수 없으므로, 위상 정렬 알고리즘 적용이 불가능
* 위상 정렬 알고리즘 구현
    * Queue를 이용한 구현
        1. 진입 차수가 0인 Node를 모두 Queue에 넣기
        2. Queue에서 하나를 꺼내고, 해당 Node에서 나가는 간선 모두 지우기
        3. 새롭게 진입 차수가 0이 된 Node들을 모두 Queue에 넣기
        4. Queue에 Node가 하나도 없을 때까지 2 ~ 3의 내용을 반복
        * Queue에 넣을 때 or Queue에서 꺼낼 때 순서를 적으면 위상 정렬 수행 순서
        ```python
        def topology_sort():
            result = []
            q = deque()
            for i in range(1, v + 1):
                if indegree[i] == 0: # 진입 차수 확인
                    q.append(i)
            
            while q:
                now = q.popleft()
                result.append(now)
                for i in graph[now]: # 현재 그래프와 연결된 값들 1씩 제거
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
            
            for i in result:
                print(i, end=' ')
        ```
    * Stack을 이용한 구현
        1. 진입 차수가 0인 Node를 모두 Stack에 넣기
        2. Stack에서 하나를 꺼내고, 해당 Node에서 나가는 간선 모두 지우기
        3. 새롭게 진입 차수가 0이 된 Node들을 모두 Stack에 넣기
        4. 모든 Node 방문이 끝나면 종료
        * Stack에 넣을 때의 순서를 적으면 위상 정렬 수행 순서
        ```python
        def topology_sort():
            result = []
            s = list()
            for i in range(1, v + 1):
                if indegree[i] == 0: # 진입 차수 확인
                    s.append(i)
                    result.append(i)
            
            while s:
                now = s.pop()
                for i in graph[now]: # 현재 그래프와 연결된 값들 1씩 제거
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        s.append(i)
                        result.append(i)
            
            for i in result:
                print(i, end=' ')
        ``` 
* 위상 정렬의 답은 하나가 아님! (한 번에 여러 개의 진입 차수가 0이 될 경우, 무엇을 먼저 넣느냐에 따라 결과가 달라짐)
![위상정렬예시](./graph_theory/위상정렬예시.png)
* 모든 원소를 방문하기 전에 Queue가 모두 비었다면, 사이클이 존재하는 것으로 판별
* 모든 Node 및 간선을 제거해야하므로 시간 복잡도는 O(N + E)

### 리뷰
* 여러가지 Graph의 활용 예시에 대해 알아보았다.
* 이름만 들어본 크루스칼 알고리즘 같은 내용을 보니 신기했다
* 내용이 특별한 것보다, 이름만 들어보고 내용을 몰랐던 것을 알아서 신기했다.
* 기존에 알고리즘 문제에서 이와 같은 예시를 본 것 같은데, 이제 풀어봐야겠다.
