class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_int = 2**31 - 1
        min_int = -2**31
        s = s.strip()
        length = len(s)
        if length == 0:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
            if sign == 1 and result > max_int:
                return max_int
            if sign == -1 and result > -min_int:
                return min_int
            
        return sign * result