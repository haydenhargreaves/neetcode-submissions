class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stk = []

        for c in s:
            if c in ['[', '(', '{']:
                stk.append(c)
            elif stk and stk[-1] == closing[c]:
                stk.pop()
            else:
                stk.append(c)


        return len(stk) == 0

        