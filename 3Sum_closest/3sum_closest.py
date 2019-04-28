class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result=sum(nums[-3:])
        
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) -1
            # 在这里可以做一个短路设计，但是我忘了。
            
            while l < r:
                _sum = sum([nums[i] + nums[l] + nums[r]]) 
                if abs(_sum - target) < abs(result - target):
                    result = _sum
                if _sum == target:
                    return target
                # 结果比目标大
                elif _sum > target:
                    r -= 1
                # 结果比目标小
                else:
                    l += 1
        
        return result
        
