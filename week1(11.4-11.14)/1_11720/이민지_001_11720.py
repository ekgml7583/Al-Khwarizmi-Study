#11720번 숫자의 합 구하기
count=int(input()) #숫자 개수 입력
number=list(map(int,input())) #number리스트에 숫자 입력(공백 없이)
total=0 #합계
for i in range(count):  #숫자 개수 만큼 반복
    total+=number[i] #total에 리스트 숫자 하나씩 더하기
print(total) #최종 합계