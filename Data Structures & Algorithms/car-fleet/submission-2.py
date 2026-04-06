class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs, reverse=True):
            nextTime = (target - p)/s
            if not stack or nextTime > stack[-1]:
                stack.append(nextTime)
        return len(stack)
