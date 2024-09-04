class Solution:
    def countPairs(self, nums: list[int]) -> int:
        def check(num0, num1):
            if(num0==num1):
                return 1
            diff_cnt=0
            val0_list=[]
            val1_list=[]
            while num0>0 or num1>0:
                m0 = num0%10
                m1 = num1%10
                if m0!=m1:
                    diff_cnt+=1
                    val0_list.append(m0)
                    val1_list.append(m1)
                    if diff_cnt==3:
                        return 0
                num0//=10
                num1//=10
            if diff_cnt!=2:
                return 0
            if val0_list[0]==val1_list[1] and val0_list[1]==val1_list[0]:
                return 1
            return 0
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                ans+=check(nums[i], nums[j])
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.countPairs([3,12,30,17,21]))