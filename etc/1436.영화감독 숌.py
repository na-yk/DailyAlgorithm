"""
#1436 영화감독 숌
부르트포스
"""
import sys

input = sys.stdin.readline().rstrip() # 입력받기

input = int(input)
count = 0
result = 666
while (count != input):
    if "666" in str(result):
        count+=1
    result+=1

print(result-1)