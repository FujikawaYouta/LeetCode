class Solution:
    def jump(self, nums: list[int]) -> int:
        '''
        考虑每一步能跳到的下一站的最远距离
        '''
        # n = len(nums)
        # if n==1:
        #     return 0
        # farthest_node = nums[0]
        # times = 1
        # cur_idx = 1
        # while farthest_node<n-1:
        #     tmp = farthest_node
        #     for node in range(cur_idx, tmp+1):
        #         farthest_node = max(farthest_node, node+nums[node])
        #     cur_idx = tmp+1
        #     times+=1
        # return times
        '''
        官解，比较简洁明了
        '''
        n = len(nums)
        farthest_node = 0
        end_node = 0
        step = 0
        for i in range(n-1):
            if farthest_node>=i:
                farthest_node = max(farthest_node, i+nums[i])
                if end_node == i:
                    end_node = farthest_node
                    step+=1
            else:
                return -1
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.jump([2,3,1,1,0,1,3]))