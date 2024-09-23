class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        if n<10:
            return n
        # 对于两位数以上的，考虑排序数A_m^n，最高位数为10位
        factorial = [1 for _ in range(11)]
        for i in range(1,11):
            factorial[i] = factorial[i-1]*i
        num_len = 0
        num = n
        while num>0:
            num//=10
            num_len+=1
        ans = 0
        last_num = [0 for _ in range(10)]
        # 从高位向低位遍历
        for i in range(num_len-1,-1,-1):
            factor = int(pow(10,i))
            cur_num = n//factor%10
            c = last_num[cur_num]
            for j in range(cur_num,10):
                last_num[j]+=1
            if cur_num-c<0:
                continue
            ans += (cur_num-c)*factorial[9]//factorial[9-i]
            # 最后一位检查自己是不是特殊数字
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.countSpecialNumbers(n=20))