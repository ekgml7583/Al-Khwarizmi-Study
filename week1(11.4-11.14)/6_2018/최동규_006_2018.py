# 연속된 자연수의 합 구하기
# 성공 여부: O

import sys
N = int(sys.stdin.readline())

#  count를 1로 초기화 하는이유는 15만 뽑는 한가지 경우의 수를 빼고 계산하는것이다.
count = 1 
start = 1
end = 1
sum = 1

while(end!= N):
    if sum == N:
        count +=1
        end +=1
        sum += end
    elif sum < N:
        end += 1
        sum += end
    else:
        sum -= start
        start+=1

print(count)