import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_croatian_letters() -> None:
    word = input().strip()

    # 크로아티아 알파벳 (변경된 입력 형태)
    patterns = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for p in patterns:
        word = word.replace(p, "*") # 한 글자로 치환

    output(str(len(word)))

count_croatian_letters()