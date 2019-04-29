#!/usr/bin/python
__author__ = ['Zhao']
__version__ = "0.0.2"

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []
        c_list = [num_dict[d] for d in digits]
        result = list(c_list[0])
        # print( result)
        for i in c_list[1:]:
            tmp_list = []
            for k in result:
                for j in i:
                    tmp_list.append(k+j)
            result = tmp_list

        return result

