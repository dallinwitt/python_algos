# Given a non-empty array of integers, return the third maximum number 
#in this array. If it does not exist, return the maximum number. 
#The time complexity must be in O(n).

def thirdMax(self, nums: List[int]) -> int:
    nums.sort()
    uniques = []
    for i in nums:
        if i not in uniques:
            uniques.append(i)
        else:
            continue
    if len(uniques) < 3:
        return uniques[-1]
    else:
        return uniques[-3]