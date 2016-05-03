class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(list(s)))


if __name__ == '__main__':
	test = Solution()
	print(test.reverseVowels('hello'))