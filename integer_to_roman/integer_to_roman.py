#!/usr/bin/python
__author__ = ['Zhao']
__version__ = "0.0.2"

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = "MDCLXVI"
        steps = [1000, 500, 100, 50, 10, 5, 1]



        result = ""


        cur = 0
        while cur < len(steps):
            mod = num // steps[cur]
            if mod < 4:
                result += symbols[cur] * mod
            elif mod == 4:
                result = result + symbols[cur] + symbols[cur-1]
            elif mod == 5:
                result = result + symbols[cur-1]
            elif 5<mod<9:
                result = result + symbols[cur-1] + symbols[cur]*(mod-5)
            else:
                result = result + symbols[cur] + symbols[cur-2]
            # print "====={}====".format(result)
            num = num % steps[cur]
            cur += 2

        return result
