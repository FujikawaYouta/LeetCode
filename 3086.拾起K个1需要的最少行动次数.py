class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        # max_neighbor_ones = 0
        # cur_neighbor_ones = 0
        # for num in nums:
        #     if num==1:
        #         cur_neighbor_ones+=1
        #         max_neighbor_ones = max(max_neighbor_ones, cur_neighbor_ones)
        #         if max_neighbor_ones==3:
        #             break
        #     elif cur_neighbor_ones!=0 and num==0:
        #         cur_neighbor_ones=0
        # if max_neighbor_ones==0:
        #     return k*2 if k<=maxChanges else -1
        # elif max_neighbor_ones==1:
        #     return k*2-2 if k-1<=maxChanges else -1
        # elif max_neighbor_ones>1:
        #     return k*2-1-max_neighbor_ones
        # return 0
        
        # 记录前缀和，用于获取指定区间的1的个数和索引号和
        n = len(nums)
        ones = [0 for _ in range(n+1)]
        ones[1] = 1 if nums[0]==1 else 0
        index_sums = [0 for _ in range(n+1)]
        for i, num in enumerate(nums):
            ones[i+1]=ones[i]+num
            index_sums[i+1]=index_sums[i]
            index_sums[i+1]+=i if num==1 else 0
                
        # 对于每一个位置
        min_step = float('inf')
        origin_k = k
        for aliceIndex, num in enumerate(nums):
            cur_step = 0
            k = origin_k
            # 1.取自己位置
            if num==1:
                k-=1
                if k==0:
                    min_step=min(min_step, cur_step)
                    continue
            # 2.取邻居位置
            if aliceIndex>0 and nums[aliceIndex-1]==1:
                k-=1
                cur_step+=1
                if k==0:
                    min_step=min(min_step, cur_step)
                    continue
            if aliceIndex<len(nums)-1 and nums[aliceIndex+1]==1:
                k-=1
                cur_step+=1
                if k==0:
                    min_step=min(min_step, cur_step)
                    continue
            # 3.取添加交换位置
            if maxChanges>=k:
                cur_step+=2*k
                min_step=min(min_step, cur_step)
                continue
            else:
                k-=maxChanges
                cur_step+=2*maxChanges
            # 4.取其余位置(二分法找d，使得[aliceIndex-d, aliceIndex-2]+
            # [aliceIndex+2, aliceIndex+d]1的个数==k)
            # d的范围是[2,|边界值-aliceIndex|]
                d_left = 2
                d_right = max(aliceIndex,n-aliceIndex)
                d = (d_right+d_left)//2
                i1 = max(0, aliceIndex-d)
                i2 = min(n, aliceIndex+d+1)
                left_ones = ones[max(0, aliceIndex-1)]-ones[i1]
                right_ones = ones[i2]-ones[min(n, aliceIndex+2)]
                cur_ones = left_ones+right_ones
                while d_left<=d_right:
                    # d太大了
                    if cur_ones>k:
                        d_right=d-1
                    else:
                        d_left=d+1
                    d = (d_right+d_left)//2
                    i1 = max(0, aliceIndex-d)
                    i2 = min(n, aliceIndex+d+1)
                    left_ones = ones[max(0,aliceIndex-1)]-ones[i1]
                    right_ones = ones[i2]-ones[min(n,aliceIndex+2)]
                    cur_ones = left_ones+right_ones
                # 特判一下
                if k>cur_ones:
                    i2+=1
                    right_ones+=1
                left_sum = index_sums[max(0,aliceIndex-1)]-index_sums[i1]
                right_sum = index_sums[i2]-index_sums[min(n, aliceIndex+2)]
                cur_step+=(left_ones*aliceIndex-left_sum)+(right_sum-right_ones*aliceIndex)  
            min_step=min(min_step, cur_step)
        return min_step
    
sol = Solution()
nums = [1,1,0,0,0,1,1,0,0,1]
k = 3
maxChanges = 1
print(sol.minimumMoves(nums,k,maxChanges))