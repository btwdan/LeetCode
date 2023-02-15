#1470. Shuffle the Array
class Solution(object):
    def shuffle(self, nums, n):
        a = []
        m = n
        for i in range (len(nums)-1):
            if(i == len(nums)/2):
                break
            a.append(nums[i])
            a.append(nums[m])
            m += 1
        return a