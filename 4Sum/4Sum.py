__author__ = ["Zhao"]
__version = "0.0.1"

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        # print(nums)
        
        # i is first
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 剩余的是一个3 sum问题
            for j in range(i+1, len(nums) - 2):
                # 注意，这里和3sum略有不同
                if j > 1 and (nums[j] == nums [j-1] and j>i+1): 
                    print(nums[i], nums[j])
                    continue
                l = j + 1
                r = len(nums) - 1
                min_sum = sum([nums[i], nums[j], nums[j+1], nums[j+2]])
                max_sum = sum([nums[i], nums[j], nums[r], nums[r-1]])
                
                # 短路设置，在这种情况下，就不用再计算了
                if min_sum > target or max_sum < target:
                    continue
                # 正常的3sum算法
                while l < r:
                    # print([nums[i], nums[j] , nums[l], nums[r]])
                    tmp_sum = sum([nums[i], nums[j] , nums[l], nums[r]])
                    
                    if tmp_sum < target:
                        l += 1
                    elif tmp_sum > target:
                        r -= 1
                    # tmp_sum = target
                    else:
                        print(i, j, l, r)
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
        return res
                    
