class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            nums=[((nums[n]+nums[n+1])%10) for n in range(len(nums)-1)]
        return nums[0]
