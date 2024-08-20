#include <vector>
#include <iostream>
using namespace std;

const int MAX_INT = 0x7fffffff;
class Solution {
public:
    int dfs(vector<int>& nums, vector<int>& andValues, int start_ptr, int end_ptr, int idx){
        int andResult = 0;
    }
    int minimumValueSum(vector<int>& nums, vector<int>& andValues) {
        int n = nums.size();
        int m = andValues.size();
        int ans = MAX_INT;
        for(int i = 0; i<=n-m; i++){
            int tmp = dfs(0, i+1, 0);
            if(tmp!=MAX_INT && tmp<ans){
                ans=tmp;
            }
        }
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1,4,3,3,2};
    vector<int> andValues = {0,3,3,2};
    cout << (sol.minimumValueSum(nums, andValues)) << endl;
    return 0;
}