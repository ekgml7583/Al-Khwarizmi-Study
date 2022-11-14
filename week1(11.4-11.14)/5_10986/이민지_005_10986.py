#10986번 나머지 합 구하기
N,M=map(int,input().split())  #N개의 수와 나눌 M입력 받기
A=list(map(int,input().split())) #N개의 수가 들어간 리스트A 입력 받기
prefix_sum=0 #누적합 0으로 초기화
remainder=[0 for i in range(M)] #remainder(나머지 리스트) 0으로 초기화
for i in range(N): #누적합 계산 및 remainder리스트 변경
    prefix_sum+=A[i] #누적합 계산
    index=prefix_sum%M #prefix_sum의 나머지를 index로 표현->0,1,..,M-1
    remainder[index]+=1 #나머지 개수

#나머지 합 문제 풀이 핵심 아이디어
#S[i]~S[j]인 경우, (S[j]-S[i-1])%M==0이므로
#전개해보면 S[j]%M-S[j-1]%M==0
#따라서 S[j]%M==S[j-1]%M인 경우를 찾으면 된다.
#즉, 나머지 값이 같은 경우를 찾기!

count=remainder[0] #nC1 고려(나머지가 0인 경우 1씩 뽑아도 되니까)
for i in range(M):
    count+=((remainder[i]*(remainder[i]-1))//2) #nC2(나머지가 같은 인덱스 중 두 개 뽑기)
print(count)