import re

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def evaluate(num1: int, num2: int, operator: str):
            num1 = int(num1)
            num2 = int(num2)

            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num2 - num1
            elif operator == "*":
                return num1 * num2
            else:
                return int(num2 / num1) 


        for char in tokens:
            if re.search(r"\d", char) is not None:
                stack.append(char)
            else:
                print('beginning of op')
                print(stack)
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(evaluate(num1, num2, char))
                print('evaluated nums appended')
                print(stack)
            
        return int(stack[0])
