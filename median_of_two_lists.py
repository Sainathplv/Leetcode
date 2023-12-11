class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        #merge/join the arrays
        nums=nums1+nums2
        #sort arrays
        nums.sort()

        #median
        n=len(nums)
        if n%2 ==0:
            return(float(nums[n//2 -1])+float(nums[n//2]))/2.0
        else:
            return float(nums[n//2])

        
