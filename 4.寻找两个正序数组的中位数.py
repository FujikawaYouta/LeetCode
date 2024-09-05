# 二分查找
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        def findKthNumber(nums1, nums2, k):
            n1 = len(nums1)
            n2 = len(nums2)
            while(k>0 and n1>0 and n2>0):
                idx1 = min((k-1)//2,n1-1)
                idx2 = min((k-1)//2,n2-1)
                if nums1[idx1]<=nums2[idx2]:
                    nums1 = nums1[idx1+1:]
                    k-=idx1+1
                    n1-=idx1+1
                else:
                    nums2 = nums2[idx2+1:]
                    k-=idx2+1
                    n2-=idx2+1
            if n1==0:
                return nums2[k]
            if n2==0:
                return nums1[k]
            return min(nums1[0],nums2[0])
        return findKthNumber(nums1, nums2, (n1+n2)//2) if (n1+n2)&1 else \
            (findKthNumber(nums1, nums2, (n1+n2)//2)+findKthNumber(nums1, nums2, (n1+n2)//2-1)) /2
    
if __name__ == '__main__':
    sol = Solution()
    # print(sol.findMedianSortedArrays(nums1 = [1,2,3,4,5], nums2 = [1,2,5,7,9]))
    # print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
    print(sol.findMedianSortedArrays(nums1 = [], nums2 = [3]))