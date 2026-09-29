class Solution:
    def isValid(self, s: str) -> bool:
        closing = { '}': '{', ']': '[', ')': '(' }
        stk = []

        for c in s:
            if c in closing.values():
                stk.append(c)
            elif stk and stk[-1] == closing[c]:
                stk.pop()
            else:
                return False
                stk.append(c)


        return len(stk) == 0

        