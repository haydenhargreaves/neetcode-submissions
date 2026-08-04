class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        maxCount = 0

        l, r = 0, k
        while r <= len(blocks):
            cur = len([char for char in blocks[l:r] if char == 'B'])
            maxCount = max(maxCount, cur)

            l += 1
            r += 1


        return k - maxCount
        