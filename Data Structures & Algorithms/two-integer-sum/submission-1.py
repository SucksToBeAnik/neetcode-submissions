class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            for jdx in range(len(nums)):
                if(idx == jdx):
                    continue
                if nums[idx] + nums[jdx] == target:
                    return [idx, jdx]

        