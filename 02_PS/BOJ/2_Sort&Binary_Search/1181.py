import sys

input = sys.stdin.readline

def sort_english_words(count: int) -> None:
    words = [input().strip() for _ in range(count)]
    
    # 중복된 영단어 제거하기
    unique_words = set(words)
    
    # (길이, 사전순) 기준으로 정렬하기
    sorted_words = sorted(unique_words, key=lambda word: (len(word), word))
    
    sys.stdout.write("\n".join(sorted_words))
    
n = int(input().strip())
sort_english_words(n)