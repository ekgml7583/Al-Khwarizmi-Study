# 구간합 구하기5
# 성공여부:

import sys
N, M = map(int, sys.stdin.readline().split())

# 1. 행렬을 계산하기 위해 0으로 구성된 임의의 배열을 초기화
Matrix = [[0]*(N+1)]
Sum_Matrix = [[0]*(N+1) for _ in range(N+1)]

# 2. 행렬을 입력받으면서 행렬의 1열을 0으로 초기화 한다.
for i in range(N):
    row = [0] + [int(x) for x in sys.stdin.readline().split()]
    Matrix.append(row)

# 3. 행렬의 구간합을 구하는 공식을 이용, 행렬의 1번째 행, 1번째 열 부터 시작하는게 포인트
for i in range(1, N+1):
    for j in range(1, N+1):
        Sum_Matrix[i][j] = (Sum_Matrix[i-1][j] + Sum_Matrix[i]
                            [j-1] - Sum_Matrix[i-1][j-1]) + Matrix[i][j]

# 4. x2, y2에 해당하는 구간 합 행렬의 값에서 해당되지않는 구간합을 빼고 중복해서 빼지는 구간 합을 더해준다.
# 예를 들어 (2,2) , (3,4) 사이의 구간합을 구하고싶다면 (3,4) 구간합에서 (1,4) 구간합을 빼고 (3,1) 구간합을 빼는데
# (1,1)의 구간합은 중복해서 빠지므로 더해줌으로써 구간합을 구할 수 있다.
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = (Sum_Matrix[x2][y2] - Sum_Matrix[x1-1][y2] -
              Sum_Matrix[x2][y1-1]) + Sum_Matrix[x1-1][y1-1]
    print(result)
