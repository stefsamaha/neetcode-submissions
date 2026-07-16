class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = "+-*/"

        for c in tokens:
            if c in operators:
                x = int(stack.pop()) #2
                y = int(stack.pop()) #1
                if c == "+":
                    res = x+y # 3
                elif c == "-":
                    res = y-x
                elif c == "*":
                    res = x*y
                else:
                    res = y/x

                stack.append(res) # 3
            
            else:
                stack.append(c)
        
        return int(stack[0])


        