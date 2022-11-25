import sys
input=sys.stdin.readline

S, P = map(int, input().split()) #DNA문자열의 길이, 부분 문자열의 길이
DNAList=list(input()) #DNA 문자열
DNAMin=list(map(int, input().split())) #부분 문자열에 포함되어야 할 A,C,G,T의 최소 개수

total=0 #만들 수 있는 비밀번호 종류의 수
start=0 #슬라이딩 윈도우의 시작점
last=P #슬라이딩 윈도우의 끝점

while(last!=S+1): #끝점이 마지막에 도달할때까지
    window=DNAList[start:last] #한칸씩 밀기
    count=[0 for j in range(4)]
    for i in range(len(window)): #윈도우에 있는 문자 카운트 세기
        if window[i] == 'A':
            count[0]+=1
        elif window[i] == 'C':
            count[1]+=1
        elif window[i] == 'G':
            count[2]+=1
        else:
            count[3]+=1
  
    if (count[0]>=DNAMin[0]) and (count[1]>=DNAMin[1]) and (count[2]>=DNAMin[2]) and (count[3]>=DNAMin[3]) : #조건을 모두 만족하는 경우 카운트 증가
            total+=1
    start+=1
    last+=1

print(total)
        

