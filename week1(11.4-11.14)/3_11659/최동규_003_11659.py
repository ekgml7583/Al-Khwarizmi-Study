# 구간합 구하기 4
# 성공여부 : O

import sys
N, M = map(int, sys.stdin.readline().split())
N_num_list = list(map(int, sys.stdin.readline().split()))
Sum_list = [0]
sum = 0
for i in N_num_list:
    sum = sum + i
    Sum_list.append(sum)
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(Sum_list[end] - Sum_list[start-1])
