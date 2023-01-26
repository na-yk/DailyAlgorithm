import sys

n = int(sys.stdin.readline().rstrip())

three = [3, 13, 23]     # 시 단위에서 3이 하나라도 있는 경우
have3 = (6*10*6*10) - (5*9*5*9)     # 분, 초 단위에 3이 하나라도 있는 경우의 수

result = 0

for i in three:
    if n < i:
        result += have3*(n+1-three.index(i))    # 시에 3이 없고 분,초에 3이 있는 경우의 수
        result += three.index(i)*(60*60)   # 시에 3이 있는 모든 경우의 수
        break

print(result)

"""
# 3중 for문 풀이법
# 탐색 대상 데이터 수가 86400개이므로 완전 탐색으로도 해결 가능

n = int(sys.stdin.readline().rstrip())
result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result+=1

print(result)
"""



