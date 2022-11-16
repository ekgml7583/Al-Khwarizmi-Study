# 나머지 합 구하기
# 성공여부 : X

import sys
N, M = map(int, sys.stdin.readline().split())
Num_L = list(map(int, sys.stdin.readline().split()))
Sum_L = []
sum = 0
count = 0
for i in range(N):
    sum = sum + Num_L[i]
    Sum_L.append(sum)
Sum_L_remain = [x % M for x in Sum_L]
count = Sum_L_remain.count(0)

for i in range(1, N):
    for j in range(i):
        if (Sum_L_remain[i] - Sum_L_remain[j]) == 0:
            count += 1
print(count)
