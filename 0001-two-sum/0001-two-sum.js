/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) { 

    //Initialize hashmap
    let hashmap = new Map()
    //Iterate through array and add complements to hashmap
    for (let i = 0; i <= nums.length; i++) {
        //Initialize complement and define
        let complement = target - nums[i]
        //Check if complement is in hashmap and if true, return answer
        if (hashmap.has(complement)) {
            return [i, hashmap.get(complement)]
        }
        //If false, complement is not present, add to hashmap
        hashmap.set(nums[i], i)
    }
};