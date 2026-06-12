class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_arr = []
        for num in nums:
            if num not in temp_arr:
                temp_arr.append(num)
            else:
                return True

        return False