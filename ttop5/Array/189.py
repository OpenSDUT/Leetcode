class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nList = []
        i = len(nums) - k
        while i < (len(nums)):
            nList.append(nums[i])
            i += 1
        for j in range(len(nums) - k):
            nList.append(nums[j])
        nums = nList
