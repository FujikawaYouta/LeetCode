#include<iostream>
#include<vector>
using namespace std;

struct QueryData
{
    long long num;
    long long offset;
    long long bit_num;
};

class Solution {
public:
    long long calPowCount(long long x, int bit_num){
        long long pow_cnt = 0;
        for(int i=1;i<bit_num;i++){
            long long cycle_len = (1LL<<(i+1));
            long long cycle_cnt = (x+1)/cycle_len;
            long long count1 = (cycle_len>>1)*cycle_cnt;
            long long count2 = (x+1)%cycle_len>(cycle_len>>1)?(x+1)%cycle_len-(cycle_len>>1):0;
            pow_cnt+=(count1+count2)*i;
        }
        return pow_cnt;
    }
    long long calOneCount(long long x, int bit_num){
        long long one_cnt = 0;
        for(int i=0;i<bit_num;i++){
            long long cycle_len = (1LL<<(i+1));
            long long cycle_cnt = (x+1)/cycle_len;
            long long count1 = (cycle_len>>1)*cycle_cnt;
            long long count2 = (x+1)%cycle_len>(cycle_len>>1)?(x+1)%cycle_len-(cycle_len>>1):0;
            one_cnt+=count1+count2;
        }
        return one_cnt;
    }
    QueryData findMaximumEdgeNum(long long query_edge){
        QueryData res;
        long long left_tmp = 0;
        long long right_tmp = 0;
        for(int i=1;i<64;i++){
            long long num = (1LL<<i)-1;
            long long one_cnt = i*(1LL<<(i-1));
            if(one_cnt==query_edge){
                res.num=num;
                res.offset=0;
                res.bit_num=i+1;
                return res;
            }
            if(one_cnt>query_edge){
                right_tmp=num;
                res.bit_num=i+1;
                break;
            }
            left_tmp=num;
        }
        long long mid_tmp;
        while(left_tmp<right_tmp){
            mid_tmp = (left_tmp+right_tmp)/2;
            long long mid_one_cnt = calOneCount(mid_tmp, res.bit_num);
            if(query_edge>=mid_one_cnt){
                res.num = mid_tmp;
                res.offset = query_edge-mid_one_cnt;
            }
            if(mid_one_cnt>query_edge)
                right_tmp = mid_tmp;
            else if(mid_one_cnt<query_edge)
                left_tmp = mid_tmp+1;
            else
                break;
        }
        return res;
    }
    int pow_mod(long long x, long long y, int mod) {
        if (mod==1)
            return 0;
        int res = 1;
        while (y) {
            if (y & 1) {
                res = res * x % mod;
            }
            x = x * x % mod;
            y >>= 1;
        }
        return res;
    }
    vector<int> findProductsOfElements(vector<vector<long long>>& queries) {
        vector<int> ans;
        // 每个数对应几个1，就说明他占用了big_nums的几个数
        // 1-1个 10-1个 11-2个 100-1个
        // 按照1，3，7，15的节点计算一共出现了多少个1

        // 反过来说，出现了多少个1要定位到某一个数
        // 先找到某个最大的数，使它的1的个数小于等于左边界
        // 先以它为左边界，再考虑减去缺少
        // 同理，先找到某个最大的数，使它的1的个数小于等于右边界
        // 先以它为右边界，再考虑加上缺少
        for(auto query:queries){
            QueryData left_query = findMaximumEdgeNum(query[0]);
            QueryData right_query = findMaximumEdgeNum(query[1]+1);
            long long left_pow_cnt = calPowCount(left_query.num,left_query.bit_num);
            long long right_pow_cnt = calPowCount(right_query.num,right_query.bit_num);
            // 处理偏移量
            // 左边界
            for(int i=0;i<64;i++){
                if(left_query.offset==0)
                    break;
                if(((left_query.num+1)>>i)&1){
                    left_pow_cnt+=i;
                    left_query.offset--;
                }
            }
            // 右边界
            for(int i=0;i<64;i++){
                if(right_query.offset==0)
                    break;
                if(((right_query.num+1)>>i)&1){
                    right_pow_cnt+=i;
                    right_query.offset--;
                }
            }
            int mod = query[2];
            // long long times = (right_pow_cnt-left_pow_cnt)/30;
            // long long factor0 = (1<<30)%mod;
            // long long factor1 = 1;
            // for(int i=0;i<times;i++){
            //     factor1 = (factor1*factor0)%mod;
            // }
            ans.push_back(pow_mod(2LL, right_pow_cnt-left_pow_cnt, mod));
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<long long> query0 = {9,9,1};
    // vector<long long> query1 = {0,4,7};
    // vector<long long> query2 = {0,12,9};
    // vector<vector<long long> > queries = {query0, query1, query2};
    vector<vector<long long> > queries = {query0};
    // cout<<sol.findProductsOfElements({{1,3,7}})<<endl;
    vector<int> ans = sol.findProductsOfElements(queries);
    return 0;
}
