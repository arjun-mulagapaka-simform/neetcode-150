class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        hashmap = sorted(hashmap.items(),key= lambda item: item[1],reverse=True)
        topkfreq = [key for key,value in hashmap]
        return topkfreq[:k]