import sys
input=sys.stdin.readline

n=int(input()) #수열의 개수 입력받기
num=[] #수열을 담을 리스트

for i in range(n):
    num.append(int(input()))  #n개의 수열 입력받기

start=1 #1부터 시작하는 자연수
s=[] #자연수 넣은 스택
result=[]
success=True
for i in range(n):
    if num[i]>=start:
        while num[i]>=start:
            s.append(start)
            start+=1
            result.append("+")
        s.pop()
        result.append("-")
    else:
        lastpop=s.pop()
        if lastpop>num[i]:
            print("No")
            success=False
            break
        else:
            result.append("-")

if success:
    for i in range(len(result)):
        print(result[i])