#include<iostream>
using namespace std;

class Solution {
public:
    long long accumulatedPriceOfNum(long long n, int x){
        long long accumulated_price = 0;
        for(int i=1;i*x-1<63;i++){
            if((n>>(i*x-1))>0){
                // 计算当前位(i*x-1)有多少个周期
                // 当前位的周期长度为 T=2^(i*x)=1<<(i*x)
                long long cycle_len = 1LL<<(i*x);
                long long cycle_cnt = (n+1)/cycle_len;
                long long price1 = cycle_cnt*(cycle_len>>1);
                long long price2 = (n+1)%cycle_len>(cycle_len>>1)?((n+1)%cycle_len)-(cycle_len>>1):0;
                accumulated_price += price1+price2;
            }
            else
                break;
        }
        return accumulated_price;
    }
    long long findMaximumNumber(long long k, int x) {
        long long num = 0;
        long long left_val = 0;
        long long right_val = 0;
        long long accumulated_price = 0;
        for(int i=1;i<=64;i++){
            accumulated_price = 0;
            num = (1LL<<i)-1;
            long long val = 1LL<<(i-1);
            for(int j=1;j*x-1<64;j++){
                if(((num)>>(j*x-1))&1)
                    accumulated_price+=val;
            }
            if(accumulated_price>k){
                right_val = num;
                break;
            }
            left_val = num;
        }
        long long mid_val = 0;
        long long ans = 0;
        while(left_val<right_val){
            mid_val = (right_val+left_val)/2;
            accumulated_price = accumulatedPriceOfNum(mid_val, x);
            if(accumulated_price<=k)
                ans = mid_val;
            if(accumulated_price>k)
                right_val = mid_val;
            else
                left_val = mid_val+1;
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    // cout<<sol.findMaximumNumber(30, 1)<<endl;
    // cout<<sol.findMaximumNumber(9, 1)<<endl;
    // cout<<sol.findMaximumNumber(7, 2)<<endl;
    cout<<sol.findMaximumNumber(3278539330613, 5)<<endl;
    return 0;
}