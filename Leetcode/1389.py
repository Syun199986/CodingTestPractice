class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result

# test = Solution()
# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
# print(test.createTargetArray(nums, index))