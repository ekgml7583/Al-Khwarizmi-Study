import sys
input=sys.stdin.readline
suNo,quizNo=map(int,input().split())
numbers=list(map(int,input().split()))
prefix_sum=[0]
temp=0

for i in numbers:
    temp=temp+i
    prefix_sum.append(temp)#합배열

for i in range(quizNo):#질의 개수만큼
    s,e=map(int,input().split()) #질의 받기
    print(prefix_sum[e]-prefix_sum[s-1]) #구간 합,e는 전체,s는 시작인덱스
