# 날짜 : 11.25
# 최솟값 찾기
# 성공여부:

# L = 3일때 
# D1 = min(A(-1), A(0), A(1))
# D2 = min(A(0), A(1), A(2))
# D3 = min(A(1), A(2), A(3))
import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
Input_L = list(map(int, sys.stdin.readline().split()))
mydeque = deque()

# deque[0][0]의 오른쪽 값이 숫자를 가리킨다. 2차원 배열을 카운팅할때와는 다른 개념

for i in range(N):
    while mydeque and mydeque[-1][0] > Input_L[i]: # 디큐의 맨끝 인덱스(새로들어온수)가 현재 값보다 크다면 
        mydeque.pop() # pop() 디큐 오른쪽에서 값을 제거한다.
    mydeque.append((Input_L[i],i)) # 일단 디큐에 넣고봄 왼쪽이 인덱스, 오른쪽이 수
    if mydeque[0][1] <= i - L: # deaue[0][1]에서 1이 인덱스쪽을 가리킨다.
                               # 요소의 인덱스가 윈도우사이즈의 첫번째 값보다 작으면
        mydeque.popleft()
    print(mydeque[0][0], end='')
    
