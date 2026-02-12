import sys

def get_max_meeting_count(meeting_list: list[tuple[int, int]]) -> int:
    # 종료 시간을 기준으로 오름차순
    # 종료 시간이 같다면, 시작 시간을 기준으로 오름차순
    meeting_list.sort(key=lambda meeting: (meeting[1], meeting[0]))
    
    max_count = 0
    last_end_time = 0
    
    for start_time, end_time in meeting_list:
        if start_time >= last_end_time:
            max_count += 1
            last_end_time = end_time
    
    return max_count

input = sys.stdin.readline

meeting_count = int(input())
meeting_list = [tuple(map(int, input().split())) for _ in range(meeting_count)]

print(get_max_meeting_count(meeting_list))