# 주몽
# 성공여부 : O

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
elements = sorted(list(map(int, sys.stdin.readline().split())))
start = 0
end = N -1 
count = 0

# 양쪽 인덱스에서 모든 경우의수를 다 거쳐가는 반복문
while(start < end):
    if elements[start] + elements[end] < M:
        start +=1
    elif elements[start] + elements[end] > M:
        end -= 1
    else:
        count += 1
        start +=1
        end -=1
print(count)

