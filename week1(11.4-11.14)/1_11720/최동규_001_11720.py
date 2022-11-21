# 11720_숫자의 합구하기
# 성공여부: O

import sys
N = int(sys.stdin.readline())
numbers = sys.stdin.readline()
result = 0
for i in range(N):
    result += int(numbers[i])
print(result)
