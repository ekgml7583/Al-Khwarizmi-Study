# 평균 / 1546
# 성공 여부: O

import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = 0
for i in range(N):
    if M < numbers[i]:
        M = numbers[i]
numbers = [(x/M)*100 for x in numbers]
result = sum(numbers)/N
print(result)
