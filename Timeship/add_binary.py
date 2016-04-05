#!/usr/bin/python
#-*- coding:utf-8 -*-

class Solution(object):
    def addBinary(self,a,b):
        '''
        type a:str
        type b:str
        type c:str
        '''
        return bin(int(a,2)+int(b,2))[2:]
if __name__ == '__main__':
    test = Solution()
    print(test.addBinary('11','1'))
