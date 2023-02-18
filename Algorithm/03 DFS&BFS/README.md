# DFS/BFS : 탐색 알고리즘
## DFS(Depth-First Search, 깊이우선탐색)
> 🍀 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘(멀리 있는 노드부터 탐색)
### 동작 방식
1. 탐색 시작 노드를 **스택**에 삽입하고 방문 처리함
2. 스택의 최상단에 있는 노드에
    - 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리함
    - 방문하지 않은 인접 노드가 없으면 최상단 노드를 꺼냄
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복함  
### 구현
- 스택을 이용하는 알고리즘이기 때문에 재귀 함수를 이용했을 때 간결하게 구현할 수 있음
#### Python
```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

## BFS(Breadth-First Search, 너비우선탐색)
> 🍀 가까운 노드부터 탐색
### 동작 방식
1. 탐색 시작 노드를 **큐**에 삽입 후 방문 처리함
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복함
### 구현
#### Python
- 큐 자료구조 기반: `deque` 라이브러리 사용
```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
"""
인접 리스트 형식으로 그래프 저장 후
visited 리스트에 모든 노드를 미방문 상태로 초기화
visited = [False] * (노드 수)  
"""
bfs(graph, 1, visited)  # bfs 함수 호출
```
## 결론 
|       |  DFS  |       BFS       |
|:-----:|:-----:|:---------------:|
| 동작 원리 |  스택   |       큐         |  
| 구현 방법 | 재귀 함수 | 큐 자료구조(`deque`) |

<br>  

-------------------------------
## 📍 자료구조 기초
> 🍀 데이터를 표현·관리·처리하기 위한 구조
- 오버플로(Overflow): 저장 공간의 수용 가능한 크기 이상으로 삽입 연산을 수행할 때 발생함
- 언더플로(Underflow): 저장 공간에 데이터가 조내하지 않는데 삭제 연산을 수행할 때 발생함

### 스택 Stack
> First In Last Out 선입후출
- Python: 구현할 때 별도의 라이브러리나 모듈이 필요하지 않음  
  - `append()` : 스택의 가장 위에 데이터를 삽입함
  - `pop()` : 스택의 가장 위에 있는 데이터를 꺼냄

### 큐 Queue 
> First In First Out 선입선출
- Python: **deque** 자료구조를 이용하여 구현할 수 있음
  - **`from collections import deque`**
- `list()` : deque 객체를 리스트 자료형으로 변경하여 반환함

### 그래프 Graph
> 연결되어 있는 객체 사이의 관계를 표현하는 자료구조
- 노드(정점vertex)와 간선(edge)으로 이루어져 있음
- 인접 행렬 또는 인접 리스트로 표현할 수 있음
#### 1️⃣ 인접 행렬
- 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
- 연결 되어 있지 않은 노드는 가중치를 무한으로 설정함(999999999 등의 값으로 초기화)
- 모든 관계를 저장하므로 노드의 개수가 많을수록 메모리 낭비
#### 2️⃣ 인접 리스트 
- 연결 리스트를 통해 모든 노드에 대하여 각 노드에 연결된 노드의 정보를 저장함
- 실제 연결된 정보만을 저장하기 때문에 메모리 효율이 높음
- 단, 연결 정보를 확인하기 위해서 연결 데이터를 하나씩 확인해야 하기 때문에 속도가 느림
- Python: 인접 리스트를 이용해서 그래프를 표현할 때도 **2차원 리스트**를 이용하면 됨
    ```python
    graph = [[] for _ in range(3)]
    
    # 노드 0에 연결된 노드 정보 저장(노드, 거리)
    graph[0].append((1,7))
    graph[0].append((2,5))
  
    graph[1].append((0,7))
    graph[2].append((0,5))
  
    print(graph)
    ```
## 📍 재귀 Recursion
> 🍀 자기 자신을 다시 호출함
- 재귀의 최대 깊이를 초과하지 않도록 해야 함(종료 조건 명시)
- 재귀 함수는 내부적으로 스택 자료구조와 동일함
  - 재귀 함수를 이용해서 스택 자료구조를 활용해야 하는 알고리즘을 구현할 수 있는 경우가 많음
  - 코드가 간결해짐
  - ex) DFS


