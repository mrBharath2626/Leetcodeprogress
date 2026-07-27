# Last updated: 7/27/2026, 11:39:40 AM
1class Solution:
2    def checkPossibility(self, nums: List[int]) -> bool:
3        nums1,nums2=nums[:],nums[:]
4        for i in range(len(nums)-1):
5            if(nums[i]>nums[i+1]):
6                nums1[i]=nums1[i+1]
7                nums2[i+1]=nums2[i]
8                break
9        return nums1==sorted(nums1) or nums2==sorted(nums2)
10        