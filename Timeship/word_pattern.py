class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        str_of_pattern = pattern
        list_of_str = str.split()
        len_of_str = len(list_of_str)
        if len_of_str!=len(str_of_pattern):
            return False
        return len(set(zip(str_of_pattern, list_of_str))) == len(set(str_of_pattern)) == len(set(list_of_str))