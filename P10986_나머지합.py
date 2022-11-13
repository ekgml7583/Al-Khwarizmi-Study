import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=list(map(int,input().split()))
s=[0]*n #수열의 개수만큼
c=[0]*m #나누어 떨어져야 하는 수
s[0]=A[0]
answer=0
for i in range(1,n):
    s[i]=s[i-1]+A[i]

for i in range(n):# 수열의 개수만큼
    remainder=s[i]%m
    if remainder==0:
        answer+=1 #맨 처음 인덱스부터 시잔하는 것들
    c[remainder]+=1 #나머지 같은 인덱스의 개수 값 증가시키기, 처음이 아닌 인텍스들

for i in range(m):# 나머지의 개수만큼
    if c[i]>1:# 0이외의 나머지 같은 인덱스들 중에서
        answer+=(c[i]*(c[i]-1)//2)#조합 공식
print(answer)

