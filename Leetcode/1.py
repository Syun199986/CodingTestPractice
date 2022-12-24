class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_len = len(nums)
        ans = []
        for i in range(0, nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

# test = Solution()
# nums = [2,7,11,15]
# target = 9
# print(test.twoSum(nums, target))