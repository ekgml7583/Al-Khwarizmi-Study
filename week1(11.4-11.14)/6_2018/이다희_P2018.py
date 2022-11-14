n=int(input())
count=1
start_index=1
end_index=1
sum=1

while end_index!=n:
    if sum==n:#합이 N과 같다면
        count+=1
        end_index+=1
        sum+=end_index
    elif sum>n:#합이 더 크다면
        sum-=start_index#합에서 시작 인덱스를 빼고
        start_index+=1#시작 인덱스를 앞으로 한칸 이동
    else:
        end_index+=1 # 합이 더 작다면
        sum+=end_index#합에 끝 인덱스를 더하기
print(count)