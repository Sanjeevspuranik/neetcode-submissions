class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First thing enumerate both arrays into pairs: [pos, s]
        pairs = [(p, s) for p, s in zip(position, speed)]
        stack = []

        # sort according to closest to target: Use position as key
        for p, s in sorted(pairs)[::-1]:
            time_to_target = (target - p) / s
            stack.append(time_to_target)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        