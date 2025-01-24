class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for i in nums:
            if i in hashmap and hashmap[i] >= 1:
                return True
            hashmap[i] = hashmap.get(i, 0) + 1
        return False
        