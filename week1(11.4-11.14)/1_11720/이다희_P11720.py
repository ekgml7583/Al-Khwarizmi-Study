# num_list=[]
# num= int(input())
# sum=0
# for i in range(num):
#     b= int(input())
#     num_list.append(b)
#     sum+=num_list[i]
#
# print(sum)
#한 줄로 입력을 받지 못함.

##############################################################################

n=input()
numbers=list(input())
sum=0

for i in numbers:
    sum=sum+int(i)

print(sum)
