class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDic = {}
        nList = []
        L = len(nums)
        for i in range(L):
            numsDic[nums[i]] = i
        for j in range(L):  # 通过索引遍历而不是通过元素遍历是为了避免出现相同元素而只在字典中存一个的问题如：[0,4,3,0] 0
            if (target-nums[j]) in numsDic and j < numsDic[target-nums[j]]:  # 后面那个条件是为了去除重复项
                nList.append(j)
                nList.append(numsDic[target-nums[j]])
        return nList
