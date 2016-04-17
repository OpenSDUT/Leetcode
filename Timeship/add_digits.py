#!/usr/bin/python
#-*- coding:utf-8 -*-

class Solution(object):
    def addDigits(self,num):
        '''
        type num:int
        rtype :int
        '''
        while num > 9:
            sum = 0
            while num:
                sum += num%10
                num = num//10
            num = sum
        return sum

    def addDigits2(self,num):
        return (num -1)%9 +1 if num else 0

if __name__ == '__main__':
    test = Solution()
    print(test.addDigits(38))
    print(test.addDigits2(38))
