class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.getDigitSquareSum(n)

        while slow != fast:
            fast = self.getDigitSquareSum(fast)
            fast = self.getDigitSquareSum(fast)
            slow = self.getDigitSquareSum(slow)
        return True if fast == 1 else False
        
    def getDigitSquareSum(self, n):
        out = 0

        while n:
            rem = n%10
            square = rem ** 2
            out += square
            n = n//10
        return out