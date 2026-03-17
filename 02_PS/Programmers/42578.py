def solution(clothes):
    clothes_dict = {}
    
    for name, kind in clothes:
        clothes_dict[kind] = clothes_dict.get(kind, 0) + 1
        
    answer = 1
    
    for count in clothes_dict.values():
        answer *= (count + 1)
        
    return answer - 1