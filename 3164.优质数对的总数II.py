from typing import List
from collections import defaultdict
from math import isqrt
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 枚举因子
        cnt = defaultdict(int)
        for num in nums1:
            if num%k!=0:
                continue
            # 枚举nums1[i]//k的因子
            num//=k
            for i in range(1,isqrt(num)+1):
                if num%i==0:
                    cnt[i]+=1
                    if i*i<num:
                        cnt[num//i]+=1
        return sum([cnt[num] for num in nums2])
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfPairs(nums1 = [30,6], nums2 = [10,2], k = 3))