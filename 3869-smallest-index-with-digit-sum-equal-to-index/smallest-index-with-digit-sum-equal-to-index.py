class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            n=nums[i]
            digit_sum = sum(int(d) for d in str(n))

            if digit_sum == i:
                return i

        return -1