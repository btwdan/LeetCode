#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        a = []
        b = False
        for i in range (len(nums)):
            for j in range(len(nums)):
                if(i == j):
                    continue
                x = nums[i] + nums[j]
                if(x == target):
                    a.append(i)
                    a.append(j)
                    b = True
            if(b == True): 
                break
        return a