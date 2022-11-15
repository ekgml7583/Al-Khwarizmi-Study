#1546번 평균 구하기
count=int(input()) #시험을 본 과목의 개수
scores=list(map(int,input().split())) #각 과목의 시험 성적
M=max(scores) #점수 중 최댓값
total=0 #변환된 점수들의 합
for i in range(count): #과목 개수만큼 반복
    total+=scores[i]/M*100 #새로운 성적 계산법: 점수/M*100
print(total/count) #새로운 계산법 성적 평균