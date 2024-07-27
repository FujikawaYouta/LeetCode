class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        # 找25，75
        five_res = n
        five_index = -1
        two_seven_index = -1
        for i in range(n)[::-1]:
            # 找到第一个5
            if num[i]=='5':
                five_index = i
                break
        if five_index != -1:
            # 找到前一个2或者7
            for i in range(five_index)[::-1]:
                if num[i]=='2' or num[i]=='7':
                    two_seven_index = i
                    break
        if two_seven_index != -1:
            five_res = n-two_seven_index-2
        # 找50，x00
        zero_res = n
        zero_index = -1
        x_five_index = -1
        for i in range(n)[::-1]:
            # 找到第一个0，此时已经可以判定被25整除，即只剩0
            if num[i]=='0':
                zero_res = n-1
                zero_index = i
                break
        if zero_index != -1:
            # 找到前一个5或者x0
            for i in range(zero_index)[::-1]:
                if num[i]=='5' or num[i]=='0':
                    x_five_index = i
                    break
        if x_five_index != -1:
            zero_res = n-x_five_index-2
        return min(five_res, zero_res)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumOperations(num = "2245047"))
    print(sol.minimumOperations(num = "2908305"))
    print(sol.minimumOperations(num = "10"))
    print(sol.minimumOperations(num = "1"))