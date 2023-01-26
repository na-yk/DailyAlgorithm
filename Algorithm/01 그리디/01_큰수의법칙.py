import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

# for i in range(1,m+1):
#     if i//k>=1 and i%k==1:
#         result += second
#     else:
#         result += first

# 가장 큰 수를 더하는 횟수 계산
count = (m//(k+1))*k    
count += m%(k+1)    

# 결과 계산
result += (count*first)
result += (m-count)*second

print(result)
