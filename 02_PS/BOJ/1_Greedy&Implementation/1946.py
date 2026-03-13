import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_new_recruits() -> None:
    test_case_count = int(input().strip())
    output_lines = []

    for _ in range(test_case_count):
        applicant_count = int(input().strip())
        applicants = [tuple(map(int, input().split())) for _ in range(applicant_count)]

        # 서류 순위 오름차순 정렬
        applicants.sort()

        selected_count = 1
        best_interview_rank = applicants[0][1]

        # 서류 순위가 더 뒤인 지원자는
        # 지금까지 본 사람들 중 면접 순위가 가장 좋은 사람보다
        # 면접 순위가 좋아야만 선발 가능
        for _, interview_rank in applicants[1:]:
            if interview_rank < best_interview_rank:
                selected_count += 1
                best_interview_rank = interview_rank

        output_lines.append(str(selected_count))

    output("\n".join(output_lines))

count_new_recruits()