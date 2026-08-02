class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            a = Counter(s[:i]).get('0', 0)
            b = Counter(s[i:]).get('1', 0)
            score = max(score, a + b)

        return score

        