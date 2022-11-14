#11720번 숫자의 합 구하기
#숫자 개수 입력
count=int(input()) 
#number리스트에 숫자 입력(공백 없이)
number=list(map(int,input())) 
#합계
total=0
#숫자 개수 만큼 반복
for i in range(count):  
    #total에 리스트 숫자 하나씩 더하기
    total+=number[i] 
#최종 합계
print(total) 