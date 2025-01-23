class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize hashmap
        hashmap = {}
        #iterate through array...len() calculates the length of the list and range() is like i++
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []