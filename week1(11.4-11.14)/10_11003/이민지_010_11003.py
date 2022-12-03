#11003번 최솟값 찾기1
from collections import deque #deque import
import sys
input=sys.stdin.readline
N, L=map(int,input().split())
num=list(map(int, input().split()))
mydeque=deque()
min_list=[]
mydeque.append((1, num[0])) #첫 번째 노드 넣기
min_list.append(mydeque[0][1])
for i in range(1,N):
    while mydeque[-1][1] >= num[i]: #새로 들어올 노드의 값이 최근 들어간 노드 값보다 작을 경우 최근 들어간 노드 값 빼기(의미 없음)
        mydeque.pop()
        if len(mydeque) == 0: #덱이 빈 경우 중단
            break
    mydeque.append((i+1,num[i])) #새로 들어온 노드 추가
    if (i+1)-L >= mydeque[0][0]: #마지막 데이터 index - 슬라이딩 윈도우 크기 >= 맨 앞 노드의 인덱스 값
        mydeque.popleft() #맨 앞 노드의 인덱스 값 제거
    min_list.append(mydeque[0][1])

for i in range(len(min_list)):
    print(min_list[i], end=' ')
        

    

