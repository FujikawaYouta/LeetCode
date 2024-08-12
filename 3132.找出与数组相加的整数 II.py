class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = n-2
        nums1.sort()
        nums2.sort()
        min_nums2 = nums2[0]
        ans = 0
        # 使用双指针遍历
        # 如果i==0就找到了答案，那么这个答案一定是最小的，
        # 有可能是nums1[2](j==1)，也有可能是nums1[1](j!=1)
        # 如果i==0没有答案，那么答案一定是nums1[0]
        # for i in range(n):
        #     for j in range(i+1,n):
        for j in range(1,n):
            valid = True
            temp = None
            if j==1:
                temp = nums1[2:]
            else:
                temp = nums1[1:j]+nums1[j+1:]
            ans = min_nums2-temp[0]
            for i in range(m):
                if temp[i]+ans!=nums2[i]:
                    valid = False
                    break
            if valid==True:
                return ans
        return min_nums2-nums1[0]
                
if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumAddedInteger(nums1 = [4,20,16,12,8], nums2 = [14,18,10]))
    print(sol.minimumAddedInteger(nums1 = [3,5,5,3], nums2 = [7,7]))
    print(sol.minimumAddedInteger(nums1 = [4,6,3,1,4,2,10,9,5], nums2 = [5,10,3,2,6,1,9]))