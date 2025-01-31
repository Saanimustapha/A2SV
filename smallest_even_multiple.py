class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        smallestEvenMultiple = n
        while True:
            if smallestEvenMultiple%2==0 and smallestEvenMultiple%n==0:
                return smallestEvenMultiple
            smallestEvenMultiple*=2
