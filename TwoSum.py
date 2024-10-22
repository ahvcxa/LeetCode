class Solution(object):
    def twoSum(self, nums, target):
        output=[0,0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if(target-nums[i]-nums[j]==0):
                        output =[i,j]
                        break
                else:
                    continue
        return output

       
        
