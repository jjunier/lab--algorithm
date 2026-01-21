# 배열의 크기(N), 덧셈 연산 횟수(M), 큰 수 연속 사용 가능 횟수(K) 입력 받기
N, M, K = map(int, input().split())

# N개의 자연수 입력 받기
data = list(map(int, input().split(' ')))

def bigN_sum(N, M, K, data):
    # 입력 받은 자연수를 저장하는 리스트 data 변수를 내림차순으로 정렬
    data.sort(reverse=True)
    
    # 가장 큰 수와 두 번째로 큰 수 정의
    first_big_num = data[0]
    second_big_num = data[1]
    
    # 가장 큰 수의 최대 기용 횟수와 두 번째로 큰 수 기용 횟수를 한 번을 더한 덧셈 그룹 정의
    sum_group = K + 1

    answer = ((first_big_num * K + second_big_num) * (M // sum_group)) + (first_big_num * (M % sum_group))

    return answer

print(bigN_sum(N, M, K, data))