class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        algo 1) time: O(n^2), space: O(1)
        loop through all possible pairs and when we find a match we return [i,j] st nums[i] + nums[j] == target
            for i ... range(len(nums)):
                for ...

                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    return []


        algo 2: time: O(n), space: O(n)
        loop over all vals in nums and check
        diff = target - nums[i] --> 7 - 3 --> nums[i] = i
        diff = target - 7 - 4 = 3 in map? yes

        return [hashmap[diff], i]

        iter i = 0: hahsmap {3:0}
        iter i = 1: hahsmap {:0}

        '''

        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            # in hashmap?
            if diff in count:
                return[count[diff], i]
            else:
                count[nums[i]] = i
        
