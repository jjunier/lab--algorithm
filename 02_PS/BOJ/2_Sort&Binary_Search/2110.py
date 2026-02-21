import sys

input = sys.stdin.readline
output = sys.stdout.write

def router_max_distance() -> None:
    home_count, router_count = map(int, input().split())
    home_coordinates = [int(input()) for _ in range(home_count)]
    home_coordinates.sort()
    
    # 거리 d로 공유기 router_count 이상의 갯수만큼 설치가 가능한지 검사
    def can_install_distance(min_distance: int) -> bool:
        installed = 1    # 첫 번째 집에 설치
        last_installed_distance = home_coordinates[0]
        
        for distance in home_coordinates[1:]:
            if distance - last_installed_distance >= min_distance:
                installed += 1
                last_installed_distance = distance
                
                if installed >= router_count:
                    return True
                
        return installed >= router_count
    
    low_distance = 1
    high_distance = home_coordinates[-1] - home_coordinates[0]
    best_distance = 0
    
    while low_distance <= high_distance:
        mid_distance = (low_distance + high_distance) // 2
        
        if can_install_distance(mid_distance):
            best_distance = mid_distance
            low_distance = mid_distance + 1
        else:
            high_distance = mid_distance - 1
            
    output(str(best_distance))
    
router_max_distance()