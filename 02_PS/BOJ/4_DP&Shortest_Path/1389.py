import sys

input = sys.stdin.readline
output = sys.stdout.write

def find_kevin_bacon_user() -> None:
    user_count, relation_count = map(int, input().split())
    INF = 10**9
    distance = [[INF] * (user_count + 1) for _ in range(user_count + 1)]
    
    for i in range(1, user_count + 1):
        distance[i][i] = 0
        
    for _ in range(relation_count):
        user_a, user_b = map(int, input().split())
        distance[user_a][user_b] = 1
        distance[user_b][user_a] = 1
        
    # Floyd-Warshall
    for mid in range(1, user_count + 1):
        for start in range(1, user_count + 1):
            for end in range(1, user_count + 1):
                if distance[start][end] > distance[start][mid] + distance[mid][end]:
                    distance[start][end] = distance[start][mid] + distance[mid][end]
                    
    min_bacon = INF
    answer_user = 0
    
    for user in range(1, user_count + 1):
        bacon_sum = sum(distance[user][1:])
        
        if bacon_sum < min_bacon:
            min_bacon = bacon_sum
            answer_user = user
            
    output(str(answer_user))
                
find_kevin_bacon_user()