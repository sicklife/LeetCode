__Author__ = ["Zhao"]
__Version__ = "0.0.1"

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] in valid_dict:
                stack.append(s[i])
            else:
                ##print(s[i])
                if not stack or  valid_dict.get(stack.pop()) != s[i]:
                    return False
        return not stack
        
