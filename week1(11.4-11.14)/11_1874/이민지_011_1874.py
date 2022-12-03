import sys
input=sys.stdin.readline

n=int(input()) #수열의 개수 입력받기
num=[] #수열을 담을 리스트

for i in range(n):
    num.append(int(input()))  #n개의 수열 입력받기

start=1 #자연수 1부터 시작
stack=[] #자연수를 담을 스택 리스트
success=True #스택 이용하여 수열 만들 수 있는지 판단
result=[] #push, pop 출력 리스트

for i in range(n):
    if num[i]>=start:  #현재 수열 값 >= 자연수 
        while num[i]>=start:
            stack.append(start) #자연수 1씩 증가하여 스택에 추가
            start+=1
            result.append("+") #push이므로 +
        stack.pop() #수열 출력하기 위해 마지막 1회만 pop하기
        result.append("-")
    else: #현재 수열 값 < 자연수
        last=stack.pop() #스택에 있는 값 꺼내기
        if last != num[i]: #꺼낸 값이 현재 수열 값이 아닌 경우
            print("NO")  #NO로 출력
            success=False #스택 이용하여 수열 만들 수 없음
            break
        else:
            result.append("-")

if success:
    for i in range(len(result)):  #result값 출력
        print(result[i])

            