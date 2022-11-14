#11660번 구간 합 구하기2
import sys
input=sys.stdin.readline #시간을 단축하기 위해 sys라이브러리 이용
a,b=map(int, input().split())#데이터의 개수, 질의 개수(합 구하는 횟수) 입력받기->공백 이용하여 두 개의 값 받기
s_list=[list(map(int,input().split())) for _ in range(a)] #구간 합 대상 이중 배열 입력 받기
prefix_sum=[[0] * (a+1) for i in range(a+1)] #(a+1)x(a+1)개의 데이터를 가진 구간 합 이중 배열 0으로 초기화
#이때 prefix_sum는 index 고려하여 a+1개의 리스트 생성 

#0행 또는 0열은 모두 0이므로 1행1열부터 계산
for i in range(1,a+1): 
    for j in range(1, a+1):
        #prefix_sum[i][j]의 값을 채우는 구간 합 공식
        prefix_sum[i][j]=prefix_sum[i][j-1]+prefix_sum[i-1][j]-prefix_sum[i-1][j-1]+s_list[i-1][j-1]
result=[] #구간 합 결과값 리스트
for _ in range(b): #b개의 질의에 대한 값 구하기
    x1,y1,x2,y2=map(int, input().split()) #질의 (x1,y1)~(x2,y2) 입력받기
    #질의 x1,y1,x2,y2에 대한 답을 구간 합으로 구하는 방법
    result.append(prefix_sum[x2][y2]-prefix_sum[x1-1][y2]-prefix_sum[x2][y1-1]+prefix_sum[x1-1][y1-1])
#질의에 대한 답 리스트 출력
for i in range(len(result)):
    print(result[i])