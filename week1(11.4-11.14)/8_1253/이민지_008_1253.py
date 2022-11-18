import sys
input=sys.stdin.readline
N=int(input()) #수의 개수
A=list(map(int, input().split()))  #N개의 수 값 A리스트
A.sort()  #리스트 정렬
count=0
for k in range(N):  #K가 N개가 될 때까지 반복
    i=0  #i와 j를 배열 A 양쪽 끝에 위치
    j=N-1
    K=A[k] 
    while(i<j):  #i와 j가 만나기 전까지 반복
        #투 포인터 이동 원칙
        if (A[i]+A[j])>K: 
            j-=1
        elif (A[i]+A[j])<K:
            i+=1
        else:
            if A[i]==K: #자기 자신이 좋은 수가 되는 경우 제외
                i+=1 
            elif A[j]==K: #자기 자신이 좋은 수가 되는 경우 제외
                j-=1
            else:
                count+=1  #count값 증가시키고
                break #프로세스 종료
print(count)
