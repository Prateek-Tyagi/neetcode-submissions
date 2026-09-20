class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # pair for matching closing parentheses to opening parentheses
    
        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        # loop in the string
        for char in s:
            # if char is the opening parentheses, add it to stack
            if char in "({[":
                stack.append(char)
            else:
                # if char is not opening parentheses then do below
                if not stack:
                    return False
                    #Does the most recent opening bracket match the current closing bracket?
                if stack.pop() != pairs[char]:
                    return False
        return not stack
        