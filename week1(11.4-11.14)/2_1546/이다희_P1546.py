# num_list=[]
# num= int(input())# 시험을 본 과목의 개수
# sum=0
# mx=0
# new_score=[]
# for i in range(num):
#     b= int(input())
#     num_list.append(b)#시험을 본 과목 점수
# for i in range(len(num_list)):
#     if mx<num_list[i]:
#         mx=num_list[i]
#
# for i in range(len(num_list)):
#     new_score.append(num_list[i]/mx)
#     sum+=new_score[i]
#
# avg=(sum/len(num_list)*100)
# print(avg)

num_list=[]
num= int(input())# 시험을 본 과목의 개수
sum=0
mx=0
new_score=[]
mylist=list(map(int,input().split()))
for i in range(len(mylist)):
    if mx<mylist[i]:
        mx=mylist[i]

for i in range(len(mylist)):
    new_score.append(mylist[i]/mx)
    sum+=new_score[i]

avg=(sum/len(mylist)*100)
print(avg)

