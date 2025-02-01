class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        for num in range(n,2*n+1):
            if num%2 == 0 and num%n == 0:
                return num
