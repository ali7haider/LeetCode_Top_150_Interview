# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    for _ in range(k):
        prev=nums[-1]
        for i in range(len(nums)):
            nums[i],prev=prev,nums[i]
                
def myReverse(nums,li,ri):
    while li < ri:
        nums[li], nums[ri] = nums[ri], nums[li]
        li += 1
        ri -= 1
def myReverseForLoop(nums,li,ri):
    prev=nums[ri]
    for i in range(li,ri+1):
        nums[i], prev = prev, nums[i]

def rotateUsingReverse(nums,k):
    n=len(nums)
    k=k%n
    myReverse(nums,0,n-k-1)
    myReverse(nums,n-k,n-1)
    myReverse(nums,0,n-1)
    print(nums)
nums=[1,2,3,4,5,6,7]
rotateUsingReverse(nums,3)

