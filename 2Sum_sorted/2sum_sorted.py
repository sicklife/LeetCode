class Solution(object):
    def twoSum(self, numbers, target):
        """
        思路和2sum相同，一遍遍历有序数组，一遍查询辅助字典，看目标值和当前值的差值，是否在辅助字典中，如果再，则返回结果并推出；
        如果不在，则添加到辅助字典中。
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        t_dict = dict()
        for i in range(len(numbers)):
            if not t_dict.get(target - numbers[i]):
                t_dict[numbers[i]] = i+1
            else:
                return [t_dict[target - numbers[i]], i+1]
