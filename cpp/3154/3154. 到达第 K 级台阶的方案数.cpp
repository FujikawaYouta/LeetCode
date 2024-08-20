#include <iostream>
using namespace std;
class Solution {
public:
    int comb(int n, int k, int* factorial){
        // 8!/5!/3! = (8*7*6)/(1*2*3)
        k = n-k > k ? n-k: k;
        long long ans = 1;
        for(int i=1;i<=k;i++){
            ans*=n-i+1;
            ans/=i;
        }
        return ans;
    }
    int waysToReachStair(int k) {
        // 向下一级 or 向上 1 2 4 8级
        // 认为n次操作2中可穿插最多n+1次操作1
        // 向上的格数范围是 [2^n-n, 2^n-1]
        // 最后到达的范围是 [2^n-n-1, 2^n]
        // 对于i次操作2，到达了k的情况，说明其执行了x次操作1
        // 2^n-x = k, x = 2^n-k
        // 所以对于i次操作2，操作数就是n+1里取2^n-k个
        // 即C^{2^n-k}_{n+1}, C^{n}_{m}=m!/(m-n)!
        int factorial[13] = {1};
        for(int i=1;i<13;i++){
            factorial[i]=factorial[i-1]*i;
        }
        int ans = 0;
        for(int i=0;i<30;i++){
            int left_val = (1<<i)-i-1;
            int right_val = 1<<i;
            if(right_val<k)
                continue;
            if(left_val>k)
                break;
            ans += comb(i+1, (1<<i)-k, factorial);
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    cout << sol.waysToReachStair(2) << endl;
    cout << sol.waysToReachStair(4083) << endl;
    return 0;
}