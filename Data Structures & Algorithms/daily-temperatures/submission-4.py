class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initilizing the output list with zeros
        output = [0] * len(temperatures)
        # empty stack and stack stores the indices, not the temp on that day, index are the days
        stack = []
        
        for i, temp in enumerate(temperatures): # enumerate gives index and its value
            while stack and temp > temperatures[stack[-1]]: # if stack is not empty and if found day with temp greater then last max temp day
                prev_index = stack.pop() #  we grab that index
                output[prev_index] = i - prev_index # calculate the numbers of days 
            stack.append(i) # if stack is empty, add days in stack
        return output
        