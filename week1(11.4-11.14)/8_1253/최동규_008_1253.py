# 좋은수 구하기
# 성공여부 : 

import sys
N = int(sys.stdin.readline())
NL = sorted(list(map(int, sys.stdin.readline().split())))
count = 0
start = 0
end = 0
for k in range(N):
    find = NL[k]
    start = 0 
    end = N-1
    while start < end:
        if NL[start] + NL[end] == find: #좋은수를 찾았을경우
            if start!= k and end != k:
                count +=1
                break
            elif start == k: #시작인덱스가 자기자신일경우
                start +=1
            elif end == k: #종료 인덱스가 자기자신일경우
                end -= 1
        elif NL[start] + NL[end] < find: # 현재 값이 두수의합보다 클경우
            start +=1   #수의 합이 작으므로 시작인덱스를 증가
        else: # 현재 값이 두수의 합보다 작을경우
            end -=1 # 수의 합이 크므로 종료인덱스를 줄여서 합을 작게하면서 찾음
print(count)