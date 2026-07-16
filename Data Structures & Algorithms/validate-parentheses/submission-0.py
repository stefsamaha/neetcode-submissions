class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = { ")":"(", "]":"[", "}":"{" }

        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    
        return True if not stack else False 
        
        
        



# It checks whether a string of brackets like "()[]{}" is valid 
# (properly opened and closed in the correct order).

# It uses a stack to store opening brackets as they appear.

# When it sees a closing bracket, it checks whether it matches the most 
# recent opening bracket in the stack.

# If all brackets match correctly and the stack is empty at the end, 
# the function returns True; otherwise, False.


        