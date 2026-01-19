def merging(nums1,nums2):
    nums1.extend(nums2)
    return nums1

def findmedian(nums1):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
print("merged array",merging(nums1,nums2),"and median is",findmedian())
