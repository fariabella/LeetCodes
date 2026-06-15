class Solution(object):
    def twoSum(self, nums, target):
        self.result=[]
        

        for i in range(len(nums)):
            if i==len(nums):
                if nums[i]==target:
                    self.result[0]=i
                else:
                    continue 
            else:
                for j in range(i+1,len(nums)):
                     if nums[i]+nums[j]==target:
                        self.result.append(i)
                        self.result.append(j)
        
        return self.result

obj=Solution()
arr1=[2,7,11,15]
sum = 9    
result=obj.twoSum(arr1, sum)
print(result)

arr2=[3,2,4]
sum = 6    
result=obj.twoSum(arr2, sum)
print(result)

arr3=[3,3]
sum = 6    
result=obj.twoSum(arr3, sum)
print(result)