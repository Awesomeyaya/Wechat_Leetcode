“”“
两次二分法，一次找first point，一次找last point。

需要注意:
1. 第二次找end point的时候，需要再重新初始化start, end = 0, len(nums)-1
2. 结束一次二分法，判断first/last落在start, end哪个上面，需要用if..else..条件

Time O(logn) Spcae O(1)
”“”

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]

        start , end = 0, len(nums)-1 
        res = [-1,-1]
        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] >= target:
                end = mid 
            else:
                start = mid 
                
        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end  
        
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) //2 
            if nums[mid] <= target:
                start = mid 
            else:
                end = mid 

        if nums[end] == target:
            res[1] = end 
        elif nums[start] == target:
            res[1] = start
            
        return res
