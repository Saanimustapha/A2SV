class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = ""
        x = str(x)
        for index in range(len(x)-1,-1,-1):
            rev_x += x[index]
        return x == rev_x
