def solution(participant, completion):
    hash_map = {}
    
    for name in participant:
        hash_map[name] = hash_map.get(name, 0) + 1
        
    for name in completion:
        hash_map[name] -= 1
        
    for name in hash_map:
        if hash_map[name] != 0:
            return name