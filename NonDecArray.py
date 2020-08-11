# Given an array nums with n integers, your task is to check if it could 
#become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for 
#every i (0-based) such that (0 <= i <= n - 2).

def checkPossibility(self, nums: List[int]) -> bool:
    count1 = 0
    count2 = 0
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            count1+=1
    for i in range(len(nums)-2):
        if nums[i]>nums[i+2]:
            count2+=1
    if count1>1 or count2>1:
        return False
    else:
        return True