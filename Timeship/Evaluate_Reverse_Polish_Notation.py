class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #处理负数的情况
        stack_of_num = []
        for i in tokens:
        	if i.isdigit() or i[1:].isdigit():
        		stack_of_num.append(int(i))
        	else:
        		n = stack_of_num.pop()
        		m = stack_of_num.pop()
        		if i == '+':
        			stack_of_num.append(n+m)
        		elif i == '-':
        			stack_of_num.append(m-n)
        		elif i == '*':
        			stack_of_num.append(n*m)
        		elif i == '/':
        			if m*n<0 and a%b!=0:
        				stack_of_num.append(m//n+1)
        			else:
        				stack_of_num.append(m//n)
        return stack_of_num.pop()

if __name__ == '__main__':
 	test = Solution()
 	print(test.evalRPN(['4','-13','5','/','+']))