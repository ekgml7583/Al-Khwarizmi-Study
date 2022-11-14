#2018번 연속된 자연수의 합 구하기
N=int(input())  #자연수 N
start_index=end_index=sum=count=1  #변수들 1로 초기화
while(end_index!=N): #end_index가 N이 될때까지 반복
    #투 포인터 이동 원칙 
    if sum>N:  
        sum-=start_index
        start_index+=1
    elif sum<N:
        end_index+=1
        sum+=end_index
    else:
        end_index+=1
        sum+=end_index
        count+=1
print(count)