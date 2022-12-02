from collections import deque #deque import
import sys
input=sys.stdin.readline
N, L=map(int,input().split())
num=list(map(int, input().split()))
# index=1
mydeque=deque()
# for i in range(N):
#     mydeque.append([index+i,num[i]])
#     if mydeque[-1][0]-mydeque[0][0]>=3:
#         mydeque.popleft()
#     else:


for i in range(N):
    #덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    while mydeque and mydeque[-1][0] > num[i]:
        mydeque.pop()
    #덱의 마지막 위치에 현재 값 저장
    mydeque.append((num[i],i))
    #덱의 1번째 위치에서부터 L의 범위를 벗어난 값(num index-L<=index)을 덱에서 제거
    if mydeque[0][1]<=i-L:
        mydeque.popleft()
    #덱의 1번째 데이터 출력
    print(mydeque[0][0], end=' ')



