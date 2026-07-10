import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []

        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for token in tokens:

            if token in operators:
                b = stack.pop()
                a = stack.pop()

                if token == "/":
                    result = int(operators[token](a, b))
                else:
                    result = operators[token](a, b)

                stack.append(result)

            else:
                stack.append(int(token))

        return stack[-1]