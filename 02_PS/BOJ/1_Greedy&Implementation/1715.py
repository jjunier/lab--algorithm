import sys
import heapq

input = sys.stdin.readline
output = sys. stdout.write

def min_compare_count() -> None:
    bundle_count = int(input().strip())
    bundles = [int(input().strip()) for _ in range(bundle_count)]

    # 카드 묶음이 1개면 비교할 필요가 없음
    if bundle_count == 1:
        output(str(0))
        return

    heapq.heapify(bundles)
    total_compare = 0

    # 가장 작은 두 묶음을 계속 합치는 것이 최적
    while len(bundles) > 1:
        first_bundle = heapq.heappop(bundles)
        second_bundle = heapq.heappop(bundles)

        merged_bundle = first_bundle + second_bundle
        total_compare += merged_bundle

        heapq.heappush(bundles, merged_bundle)

    output(str(total_compare))

min_compare_count()