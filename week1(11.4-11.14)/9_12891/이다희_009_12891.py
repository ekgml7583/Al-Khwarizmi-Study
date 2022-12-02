#초기화 비밀번호 용량이 4개
checkList=[0]*4
myList=[0]*4
checkSecret=0

#겹치는 문자 개수 증가
def myadd(c):
    global checkList,myList, checkSecret
    if c=='A':# A이면 현재 상태리스트에 증가
        myList[0]+=1
        if myList[0]==checkList[0]:#비밀번호 체크 리스트에 있는 값과 현재 상태 리스트와 같다면 충족변수 증가
            checkSecret+=1
    elif c=='C':# C이면 현재 상태리스트에 증가
        myList[1]+=1
        if myList[1]==checkList[1]:#비밀번호 체크 리스트에 있는 값과 현재 상태 리스트와 같다면 충족변수 증가
            checkSecret+=1
    elif c=='G':# G이면 현재 상태리스트에 증가
        myList[2]+=1
        if myList[2]==checkList[2]:#비밀번호 체크 리스트에 있는 값과 현재 상태 리스트와 같다면 충족변수 증가
            checkSecret+=1
    elif c=='T':# T이면 현재 상태리스트에 증가
        myList[3]+=1
        if myList[3]==checkList[3]:#비밀번호 체크 리스트에 있는 값과 현재 상태 리스트와 같다면 충족변수 증가
            checkSecret+=1


#제거되는 문자를 처리
def myremove(c):
    global checkList,myList,checkSecret
    if c=='A':#A 이면 해당 문자 삭제하기 위해 충족변수 하나 삭제 그리고 현재 상태리스트 감소
        if myList[0]==checkList[0]:
            checkSecret-=1
        myList[0]-=1
    elif c=='C':#C 이면 해당 문자 삭제하기 위해 충족변수 하나 삭제 그리고 현재 상태리스트 감소
        if myList[1]==checkList[1]:
            checkSecret-=1
        myList[1]-=1
    elif c=='G':#G 이면 해당 문자 삭제하기 위해 충족변수 하나 삭제 그리고 현재 상태리스트 감소
        if myList[2]==checkList[2]:
            checkSecret-=1
        myList[2]-=1
    elif c=='T':#T 이면 해당 문자 삭제하기 위해 충족변수 하나 삭제 그리고 현재 상태리스트 감소
        if myList[3]==checkList[3]:
            checkSecret-=1
        myList[3]-=1


#입력받기 s=전체 리스트 수 p=부분 문자열 리스트 수 a= 전체 리스트 checkList=충족해야하는 문자의 수
s,p=map(int,input().split())
result=0
a=list(input())
checkList=list(map(int,input().split()))


#checkList가 0이면 최소 0이상이라는 거기에 checkSecret를 증가
for i in range(4):
    if checkList[i]==0:
        checkSecret+=1


#초기 p부분 문자열 생성
for i in range(p):
    myadd(a[i])


#4자리 수가 충족되면 result 증가
if checkList==4:
    result+=1



#앞으로 가면서 부분문자열 조건에 충족하는지 
for i in range(p,s):
    j=i-p#i는 뒤 포인터, j는 앞 포인터
    myadd(a[i])#새롭게 추가된 문자를 myList에 추가
    myremove(a[j])#윈도우 슬라이스가 움직이면 앞 포인터가 가리키는 원소 하나 제거
    if checkSecret==4:#4자리 수가 충족되면 result 증가
        result+=1

print(result)