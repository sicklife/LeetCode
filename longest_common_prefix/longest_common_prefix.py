#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Zhao']
__version__ = "0.0.2"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        for t in zip(*strs):
            if len(set(t)) > 1:
                break
            else:
                common_prefix += t[0]

        return common_prefix

