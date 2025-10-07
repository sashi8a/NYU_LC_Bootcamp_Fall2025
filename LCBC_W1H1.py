class Solution:
  def twoSum(self, numbers, target):

    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1





class Solution:
    def productExceptSelf(self, nums):
        
        prefix = []
        postfix = []

        pre = 1
        post = 1
        for i in range (len(nums)):
            prefix.append(pre)
            postfix.append(post)
            pre*=nums[i]
            post*=nums[len(nums)-1-i]

        return [pe*po for pe,po in zip(prefix,postfix[::-1])]



class Solution:
  def sortColors(self, nums):
  
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
      if nums[mid] == 0:  
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
      elif nums[mid] == 1:  
        mid += 1
      else:  
        nums[high], nums[mid] = nums[mid], nums[high]
        high -= 1



