#include<iostream>
#include<vector>
#include<numeric>
using namespace std;

class Solution {
public:
    bool dfs(vector<int> nums,int state,int cur_val,int target,vector<bool>& visited){
        if(state==0)
            return true;
        // 剪枝
        if(visited[state])
            return false;
        visited[state]=true;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(!((1<<i)&state))
                continue;
            if(cur_val+nums[i]>target)
                break;
            int next_state=state&(~(1<<i));
            int next_val=cur_val+nums[i]==target?0:cur_val+nums[i];
            if(dfs(nums, next_state, next_val, target, visited))
                return true;
        }
        return false;
    }
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum=accumulate(nums.begin(), nums.end(), 0);
        if(sum%k!=0)
            return false;
        sort(nums.begin(), nums.end());
        int target=sum/k;
        if(nums[0]>target)
            return false;
        int n=nums.size();
        vector<bool> visited((1<<n)-1, false);
        return dfs(nums,(1<<n)-1,0,target,visited);
    }
};

int main()
{
    Solution sol;
    // vector<int> nums = {4, 3, 2, 3, 5, 2, 1};//1 2 2 3 3 4 5
    vector<int> nums = {4,16,5,3,10,4,4,4,10};
    cout<<sol.canPartitionKSubsets(nums,3);
    return 0;
}