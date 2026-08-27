class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # indexing in very important 
        # stack will store pairs: [temp, index]
        stack = []

        # res stores No. of days waited to get Temp increase
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            
            stack.append([t, i])
        
        return res
                