#include<iostream>
using namespace std;

class Solution {
public:
    long long minEnd(int n, int x) {
        // 需要保留第一个数的所有结构
        // 对于0可以取1/0，对于1必须取1
        // 中间的数可以有2^n-1个，
        // 其中n为0的个数，m为1的个数，-1是除去自己
        // 如果2^n大于等于n，那么从这些数里找，
        // 如果2^n小于n，需要再补一位0，数量变为2^(n+1)
        int bit_num = 0;
        int zero_cnt = 0;
        int zero_tmp = 0;
        for(int i=0;i<32;i++){
            if((x>>i)&1){
                zero_cnt+=zero_tmp;
                zero_tmp=0;
                bit_num=i;
            }
            else{
                zero_tmp++;
            }
        }
        long long ans = 0;
        while((1LL<<zero_cnt)<n){
            zero_cnt++;
            bit_num++;
        }
        long long index = n-1;
        int ptr = 0;
        for(int i=0;i<bit_num+1;i++){
            if(i<32 && (x>>i)&1){
                ans|=(1LL<<i);
                continue;
            }
            else{
                // 取index的第i位
                ans|=((index&(1LL<<ptr))<<(i-ptr));
                ptr++;
            }
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    // cout<<sol.minEnd(5,4)<<endl;
    // cout<<sol.minEnd(4,1)<<endl;
    // cout<<sol.minEnd(3,1)<<endl;
    // cout<<sol.minEnd(2,4)<<endl;
    cout<<sol.minEnd(6715154,7193485)<<endl;
    return 0;
}