class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num<=0:
        	return False
        logx = math.log10(num)/math.log10(4)
        return True if logx-int(logx) == 0 else False

if __name__ == '__main__':
	test = Solution()
	print(test.isPowerOfFour(5))