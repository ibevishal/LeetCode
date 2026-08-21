class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        l=len(nums)
        if l<2:
            return 0
        
        nums.sort()
        diff=float("-inf")
        for i in range(l-1,0,-1):
            dif=nums[i]-nums[i-1]
            if diff<dif:
                diff=dif
        return diff