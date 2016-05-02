class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_of_vowels = ['a','e','i','o','u','A','E','I','O','U']
        list_s = list(s)
        start,end =0,len(s)-1
        while start<end:
        	if list_s[start] in list_of_vowels and list_s[end] in list_of_vowels:
        		list_s[start],list_s[end] = list_s[end],list_s[start]
        		start+=1
        		end-=1
        	elif list_s[start] not in list_of_vowels:
        		start+=1
        	elif list_s[end] not in list_of_vowels:
        		end-=1
        return ''.join(list_s)

if __name__ == '__main__':
	test = Solution()
	print(test.reverseVowels('leetcode'))