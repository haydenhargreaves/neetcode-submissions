class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            chars = [0] * 26
            for char in word:
                i = ord(char)-97
                chars[i] += 1
            key = ','.join([str(char) for char in chars])
            hash[key] = hash.get(key, []) + [word]

        res = []
        for words in hash.values():
            res.append(words)

        return res
        