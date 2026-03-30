class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #iterate through the input and push the indicies onto the stack
        # when we are at the enxt vlaue we will check if that day is warmer than the previous, if it is then we pop() from the stack
       # need to compute the difference between the indicies and stoer them in the res array
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res
     

            
