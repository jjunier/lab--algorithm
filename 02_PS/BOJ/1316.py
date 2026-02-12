import sys

def is_group_word(word: str) -> bool:
    seen = set()
    prev_char = None
    
    for character in word:
        if character != prev_char:
            # 이전에 등장한 문자가 다시 등장 시, 그룹 단어가 아님
            if character in seen:
                return False
            seen.add(character)
            prev_char = character
            
    return True
    
input = sys.stdin.readline

word_count = int(input().strip())
group_word_count = 0

for _ in range(word_count):
    word = input().strip()
    
    if is_group_word(word):
        group_word_count += 1
        
print(group_word_count)