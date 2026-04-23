class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.getDigitSquareSum(n)
            if n == 1:
                return True
        return False
        
    def getDigitSquareSum(self, n):
        out = 0

        while n:
            rem = n%10
            square = rem ** 2
            out += square
            n = n//10
        return out