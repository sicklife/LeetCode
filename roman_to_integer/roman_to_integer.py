__author__ = ["Zhao"]
__version__ = '0.0.1'

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman_int_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        i=0
        while i < len(s):
            sub_s = s[i:i+2]
            if roman_int_dict.get(sub_s):
                result += roman_int_dict.get(sub_s)
                i += 2
            else:
                result += roman_int_dict.get(s[i])
                i+=1        
        
        return result
