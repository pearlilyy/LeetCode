# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        box = []
        for i in range(0, len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < len(nums) and j < k:
                while k > 0 and k > j:
                    if nums[i]+nums[j]+nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in box:
                            box.append([nums[i], nums[j], nums[k]])
                        j += 1
                    elif nums[i]+nums[j]+nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
        return box
