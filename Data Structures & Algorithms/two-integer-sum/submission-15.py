class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            new_target = target - n

            if new_target in nums and i != indices[new_target]:
                return [i, indices[new_target]]
        return []

