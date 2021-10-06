from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = deque()

        for i, char in enumerate(chars):
            if char == "(":
                stack.append(i)
            elif char == ")" and len(stack):
                stack.pop()
            elif char == ")":
                chars[i] = ""

        for index in stack:
            chars[index] = ""

        return "".join(chars)
