class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        seen = {}

        for i in nums:
            if i in seen:
                return True 
            return False