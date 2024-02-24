# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import defaultdict
def majorityElement(nums):
    m = defaultdict(int)
    n = len(nums)
    for i in nums:
        m[i]+=1
    n=n//2
    for key,value in m.items():
        if value>n:
            return key
def majorityElementNSquare(nums):
        num=0
        overall=0
        for i in range(len(nums)):
            current=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    current+=1
            if current>overall:
                overall=current
                num=nums[i]
        return num
def majorityElementWithDictWithoutDefaultDict(nums):
    m={}
    for i in nums:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    maxKey=None
    maxValue=float('-inf')
    for key,value in m.items():
        if value>maxValue:
            maxValue=value
            maxKey=key
    return maxKey
def majorityElementWithDictWithDefaultDict(nums):
    m=defaultdict(int)
    for i in nums:
        m[i]+=1
    maxKey=None
    maxValue=float('-inf')
    for key,value in m.items():
        if value>maxValue:
            maxKey=key
            maxValue=value
    return maxKey


nums1 = [2,2,1,1,1,2,2]
nums2 = [2,2,1,1,1,2,2]
nums3 = [2,2,1,1,1,2,2]
nums4 = [2,2,1,1,1,2,2]
print('majorityElement',majorityElement(nums1))
print('majorityElementNSquare ',majorityElementNSquare(nums2))
print('majorityElementWithDictWithoutDefaultDict',majorityElementWithDictWithoutDefaultDict(nums3))
print('majorityElementWithDictWithDefaultDict',majorityElementWithDictWithDefaultDict(nums4))
