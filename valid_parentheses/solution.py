from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = deque()
        brackets = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if len(stack) < 1:
                    return False
                if bracket == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
