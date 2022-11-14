#11659번 구간 합 구하기1
a,b=map(int,input().split())#데이터의 개수, 질의 개수(합 구하는 횟수) 입력받기->공백 이용하여 두 개의 값 받기
s_list=list(map(int,input().split())) #구간 합 대상 배열 입력 받기

prefix_sum=[0 for i in range(a)]  #a개의 데이터를 가진 구간 합 배열 0으로 초기화
prefix_sum[0]=s_list[0] #처음 구간 합=배열의 첫번째 값
for i in range(a):  #구간 합 구하는 반복문
    prefix_sum[i+1]=prefix_sum[i]+s_list[i+1] #누적합 구하기
    if i+2==a: #데이터 개수가 다 채워지면 중지
        break

result=[]  #구간 합 결과값 리스트
for i in range(b): #구간 합 구하는 횟수만큼 반복
    s,f=map(int,input().split()) #구간합 시작과 끝 (prefix_sum의 인덱스는 0부터 시작이므로 -1을 해야함)
    if s-2<0: #구간 합 시작이 0보다 작을 경우(s-2를 한 이유는 구간합 시작의 바로 앞의 인덱스를 고려)
        result.append(prefix_sum[f-1]) #구간합 끝을 result에 추가
    else:
        result.append(prefix_sum[f-1]-prefix_sum[s-2]) #구간합 끝에서 구간합 시작의 앞부분 빼기
for i in range(len(result)): 
    print(result[i]) #구간 합 결과값 리스트 출력