class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in pairs:
                # closing bracket — check if stack top matches its opener
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                # opening bracket — push it
                stack.append(i)
        
        # if stack is empty, every opener found its closer
        return len(stack) == 0