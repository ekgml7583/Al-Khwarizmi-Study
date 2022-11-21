# import sys
# input=sys.stdin.readline
# N=int(input())
# result=0
# a=list(map(int,input().split()))
# a.sort()

# for n in N:
#     a[n]=find
#     i=0
#     j=0
#     while j>i:
#         if a[i]+a[j]==find:
#             result+=1
#         elif a[i]+a[j]<find:
#             i+=1
#         else :
#             j-=1
# print(result)



import sys
input=sys.stdin.readline
N=int(input())
result=0
a=list(map(int,input().split()))
a.sort()

for n in range(N):
    find=a[n]
    i=0
    j=N-1#0부터 시작하니 
    while j>i:
        if a[i]+a[j]==find:#여기서 find는 서로 다른 두 수의 합이어야 하기에 확인을 해야함
            if i!=n and j!=n:#서로 다른 두 수고 find이기에 result 수 증가
                result+=1
                break
            elif i==n:
                i+=1
            elif j==n:#j가 n과 같으니 뒤로 한칸씩 물러나기
                j-=1
        elif a[i]+a[j]<find:#find보다 작으면 i를 증가
            i+=1
        else :#find보다 크면 가장 앞서 있는 포인트 j를 하나 감소
            j-=1
print(result)
