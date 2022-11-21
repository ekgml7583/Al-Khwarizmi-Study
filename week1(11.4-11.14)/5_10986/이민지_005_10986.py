#10986번 나머지 합 구하기
N,M=map(int,input().split())  
A=list(map(int,input().split()))
i=prefix_sum=0
remainder=[0 for i in range(M)]
for i in range(N): 
    prefix_sum+=A[i]
    index=prefix_sum%M
    remainder[index]+=1

count=remainder[0]
for i in range(M):
    count+=((remainder[i]*(remainder[i]-1))//2)
print(count)