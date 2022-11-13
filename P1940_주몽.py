import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
a=list(map(int,input().split()))
a.sort()
i=0
j=n-1
count=0

while i<j:
    if a[i]+a[j]<m:#앞 포인터와 뒤 포인터가 재료의 합보다 작으면
        i+=1 #앞 포인터를 한 칸 가기-앞으로 갈수록 수가 크기에
    elif a[i]+a[j]>m:#크면
        j-=1#뒤 포인터를 한 칸 뒤로 가기-뒤록 갈수록 수가 작기에
    else:#재료의 합이면
        count+=1#count하기
        i+=1#앞으로 가기
        j-=1#뒤 포인터 뒤로 가기

print(count)