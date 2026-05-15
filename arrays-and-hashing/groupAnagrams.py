class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]
        groups = []
        for v in hashmap.values():
            groups.append(v)
        return groups