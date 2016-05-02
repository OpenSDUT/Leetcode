class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for enum in nums:
        	if enum == 0:
        		nums.remove(enum)
        		nums.append(enum)
        		print(nums)
        return nums

if __name__ == '__main__':
	test = Solution()
	print(test.moveZeroes([0,0,1]))