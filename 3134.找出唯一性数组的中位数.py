from collections import Counter

class Solution:
    def medianOfUniquenessArray(self, nums: list[int]) -> int:
        def checkLower(t: int) -> int:
            cnt = Counter()
            i = 0
            total = 0
            for j, num in enumerate(nums):
                cnt[num]+=1
                while len(cnt)>t:
                    cnt[nums[i]]-=1
                    if(cnt[nums[i]]==0):
                        del cnt[nums[i]]
                    i+=1
                total+=j-i+1
            return total
        n = len(nums)
        if n == 1:
            return 1
        t_l = 1
        t_r = n
        t_mid = -1
        mid_num = (n*(n+1)//2+1)//2
        ans = 0
        while(t_l<t_r):
            t_mid = (t_r+t_l)//2
            lower_t = checkLower(t_mid)
            if lower_t>mid_num:
                ans = t_mid
                t_r = t_mid
            elif lower_t<mid_num:
                t_l = t_mid+1
            else:
                return t_mid
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.medianOfUniquenessArray([68,65]))
                
        