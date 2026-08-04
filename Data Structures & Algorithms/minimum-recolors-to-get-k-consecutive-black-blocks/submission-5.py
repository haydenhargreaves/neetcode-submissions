class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k

        cur = len([char for char in blocks[l:r] if char == 'B'])
        maxCount = cur
        while r < len(blocks):
            l += 1
            r += 1

            if blocks[r-1] == 'B':
                cur += 1
            if blocks[l-1] == 'B':
                cur -= 1

            maxCount = max(maxCount, cur)

        return k - maxCount
        