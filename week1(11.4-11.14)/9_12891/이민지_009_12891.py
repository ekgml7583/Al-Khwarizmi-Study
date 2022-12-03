import sys
input=sys.stdin.readline

S, P = map(int, input().split()) #DNA문자열의 길이, 부분 문자열의 길이
DNAList=list(input()) #DNA 문자열
DNAMin=list(map(int, input().split())) #부분 문자열에 포함되어야 할 A,C,G,T의 최소 개수

total=0 #만들 수 있는 비밀번호 종류의 수

countA=countC=countG=countT=0 #윈도우 범위 내에 들어있는 A,C,G,T의 개수

def add(c):  #윈도우 범위내에 있는 DNA A,C,G,T의 개수 더하기
    global countA, countC, countG, countT
    if c=='A':
        countA+=1
    elif c=='C':
        countC+=1
    elif c=='G':
        countG+=1
    elif c=='T':
        countT+=1

def remove(r):  #윈도우 범위내에 없는 DNA A,C,G,T의 개수 빼기
    global countA, countC, countG, countT
    if r=='A':
        countA-=1
    elif r=='C':
        countC-=1
    elif r=='G':
        countG-=1
    elif r=='T':
        countT-=1
    
def check():  #유효한 비밀번호인지 확인
    global total
    #각 문자가 최소 개수보다 같거나 많은지 확인
    if countA>=DNAMin[0] and countC>=DNAMin[1] and countG>=DNAMin[2] and countT>=DNAMin[3]:
        total+=1

for i in range(P):  #DNAList의 0부터 P까지(즉 윈도우 범위)의 DNA 요소 개수 세기
    add(DNAList[i])

check()  #유효한지 확인  

for i in range(P,S): #윈도우크기를 고정하면서 추가되는 문자와 제거되는 문자 개수 변경(중간 범위는 따로 건들이지 않음)
    add(DNAList[i])
    remove(DNAList[i-P])
    check() #조건 확인

print(total)