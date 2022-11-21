# 나머지 합 구하기
# 성공여부 : O

import sys
N, M = map(int, sys.stdin.readline().split())
Num_L = list(map(int, sys.stdin.readline().split()))
Sum_L = []
sum = 0
C = [0]*M
count = 0
# 구간합 배열을 N으로 나눠서 나머지가 0인 경우는 N으로 나눠지는 경우의수
for i in range(N):
    sum = sum + Num_L[i]
    Sum_L.append(sum)

for i in range(N):
    r = Sum_L[i] % M
    if r == 0:
        count += 1
    C[r] += 1

for i in range(M):
    if C[i] > 1:
        count += (C[i] * (C[i] - 1) // 2 )

print(count)