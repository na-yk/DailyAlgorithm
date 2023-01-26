import sys

n, m = map(int, sys.stdin.readline().split())
min_list = []
result = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))  # 한 행 입력 받기
    min_list.append(min(row))   # 이 행에서 가장 작은 수 리스트(min_list)에 넣기

result = max(min_list)  # 가장 작은 수를 모아 놓은 리스트에서 가장 큰 수 찾기

print(result)