def solution(money):
    def rob(nums):
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1

    return max(rob(money[:-1]), rob(money[1:]))