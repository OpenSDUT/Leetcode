#!/usr/bin/python
#-*- coding:utf-8 -*-
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #判断一个数是不是三的幂，递归
        if n == 0:
        	return False
        elif n == 1:
        	return True
        else:
        	if(n%3 == 0):
        		return self.isPowerOfThree(n/3)
        	else:
        		return False
    def isPowerOfThree2(self,n):
    	'''利用log10函数，如果一个数是三的幂，则log以3为底的对数为整数
    	   如果利用log函数会有精度问题
    	'''
    	if n<=0:
    		return False
    	logx = math.log10(n)/math.log10(3)
    	return True if logx-int(logx) == 0 else False

if __name__ == '__main__':
	test = Solution()
	print(test.isPowerOfThree2(243))