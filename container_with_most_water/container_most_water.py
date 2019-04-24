#!/usr/bin/python
__author__ = ['Zhao']
__version__ = "0.0.2"
class Solution(object):
    # ref https://leetcode.com/problems/container-with-most-water/solution/
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # use index
        L, R = 0, len(height)-1
        m_area = min(height[L], height[R]) * (R-L)
        while L < R:
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
            m_area = max(min(height[L], height[R]) * (R-L), m_area)
        return m_area

