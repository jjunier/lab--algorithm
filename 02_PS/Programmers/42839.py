from itertools import permutations

def solution(numbers):
    num_set = set()

    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num_set.add(int(''.join(perm)))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in num_set:
        if is_prime(num):
            count += 1

    return count