class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<s:
            return 0
        l = 0
        r = 0
        mini = len(nums)+1
        while(r<len(nums)):
            r = r+1
            if sum(nums[l:r]) >= s:
                mini = min(mini,r-l)
                while(l<r):
                    if sum(nums[l+1:r]) >= s:
                        mini = min(mini,r-l-1)
                    else:
                        break
                    l=l+1
                        
        return mini
