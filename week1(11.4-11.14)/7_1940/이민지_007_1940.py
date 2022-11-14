#1940번 주몽의 명령
N=int(input()) #재료의 개수
M=int(input()) #갑옷이 완성되는 번호의 합
A=list(map(int, input().split())) #재료들
s=0 #i는 0부터(앞 인덱스 부터)
f=N-1  #j는 N-1부터(뒤 인덱스 부터)
count=0
A.sort() #A 오름차순으로 정렬
while(s<f): #i와 j가 만날 때까지 반벅
    #투 포인터 이동 원칙
    if (A[s]+A[f])>M:
        f-=1
    elif (A[s]+A[f])<M:
        s+=1
    else:
        s+=1
        f-=1
        count+=1
print(count)