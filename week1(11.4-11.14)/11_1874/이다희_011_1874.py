###오류 발생 


#수열의 개수 
n=int(input())
#수열의 개수만큼 초기화하는 수열리스트
a=[0]*n

for i in range(n):
    a[i]=int(input())

#담을 스택
stack=[]
#자연수 1부터 시작하고자
num=1

#수열 표현할 수 없을 경우를 표현하고자
result=True
answer=" "

for i in range(n):
    s=a[i]#수열리스트 i번째 수를 현재 수열값에 저장
    if s>num:
        while s>num:#현재 수열값이 자연수보다 크면
            stack.append(num)#자연수를 계속 스택에 저장
            num+=1#자연수를 1씩 증가
            answer+="+\n"#answer에 +를 저장
        stack.pop()#while문을 벗어나면 스택에서 제거
        answer+="-\n"#answer에 -를 저장
    else:
        k=stack.pop()
        if k>s:#스택에 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
            print("NO")
            result=False#result값을 F로 저장
            break
        else:
            answer+="-\n"#아니면 answer에 -저장

if result:#NO값을 출력한 적이 없으면 answer를 출력
    print(answer)
