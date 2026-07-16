class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)] # array of pairs from both lists
        stack = []

        for p, s in sorted(pair)[::-1]:  # reverse sorted order
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # stack has at least 2 cars and top takes less time to get to destination
                stack.pop()

        return len(stack)

        
        