class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char)-ord('a')] += 1
            key = ','.join([str(char) for char in chars])
            hash[key].append(word)

        return list(hash.values())