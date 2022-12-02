# DNA 비밀번호
# 슬라이딩 윈도우 알고리즘
# 성공여부 : 이해안됨

# min_num[0] = A
# min_num[1] = C
# min_num[2] = G
# min_num[3] = T
import sys

DNA_COUNT =[0] * 4
MIN_NUM = [0] * 4
checkSecret = 0


def myadd(c):
    global DNA_COUNT, MIN_NUM, checkSecret
    if c == 'A':
        DNA_COUNT[0] +=1
        if MIN_NUM[0] == DNA_COUNT[0]:
            checkSecret += 1
    elif c == 'C':
        DNA_COUNT[1] +=1
        if MIN_NUM[1] == DNA_COUNT[1]:
            checkSecret += 1
    elif c == 'G':
        DNA_COUNT[2] += 1
        if MIN_NUM[2] == DNA_COUNT[2]:
            checkSecret += 1
    elif c == 'T':
        DNA_COUNT[3] += 1
        if MIN_NUM[3] == DNA_COUNT[3]:
            checkSecret += 1

def myremove(c):
    global DNA_COUNT, MIN_NUM, checkSecret
    if c == 'A':
        if MIN_NUM[0] == DNA_COUNT[0]:
            checkSecret -= 1
        DNA_COUNT[0] -= 1
    elif c == 'C':
        if MIN_NUM[1] == DNA_COUNT[1]:
            checkSecret -= 1
        DNA_COUNT[1] -= 1
    elif c == 'G':
        if MIN_NUM[2] == DNA_COUNT[2]:
            checkSecret -= 1
        DNA_COUNT[2] -= 1
    elif c == 'T':
        if MIN_NUM[3] == DNA_COUNT[3]:
            checkSecret -= 1
        DNA_COUNT[3] -= 1

S, P = map(int, sys.stdin.readline().split())
DNA = list(sys.stdin.readline())
MIN_NUM = list(map(int,sys.stdin.readline().split()))
count=0

for i in range(4):
    if MIN_NUM[i] ==0:
        checkSecret += 1

for i in range(P):
    myadd(DNA[i])
if checkSecret == 4:
    count += 1

for i in range(P, S):
    j = i - P
    myadd(DNA[i])
    myremove(DNA[j])
    if checkSecret ==4:
        count += 1

print(count)
    
