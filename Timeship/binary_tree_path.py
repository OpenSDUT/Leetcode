# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

    	if not root:
    		return []
    	if not root.left and not root.right:
    		return [str(root.val)]
    	
    	list_of_left = self.binaryTreePaths(root.left)
    	list_of_right = self.binaryTreePaths(root.right)

    	left = [str(root.val)+'->'+str(left_path) for left_path in list_of_left]
    	right = [str(root.val)+'->'+str(right_path) for right_path in list_of_right]

    	return left+right

if __name__=='__main__':
	test = Solution()