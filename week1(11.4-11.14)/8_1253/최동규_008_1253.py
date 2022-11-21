# 좋은수 구하기
# 성공여부 : 

import sys
N = int(sys.stdin.readline())
NL = sorted(list(map(int, sys.stdin.readline().split())))
count = 0
start = 0
end = 0
for i in range(N):
    k = NL[i]
    start = 0 
    end = N-1
    while start < end:
        if NL[start] + NL[end] == k:
            if start!= k and end != k:
                
        elif(NL[start] + NL[end]) < k:
            start +=1
        else:
            end =+1
