#include <iostream>
#include <vector>
using namespace std;

const int mod = (int)1e9+7;
class Solution {
public:
    int checkRecord(int n) {
        // dp0[i][j][k] 代表Absence  结尾的长度为i的缺席数为j的连续迟到k次的合法排列数
        // dp0[i][j][k] 代表Late     结尾的长度为i的缺席数为j的连续迟到k次的合法排列数
        // dp0[i][j][k] 代表Presence 结尾的长度为i的缺席数为j的连续迟到k次的合法排列数
        // k=0,1, ok
        // k=2, 不ok
        vector<vector<vector<int> > > dp0(n+1, vector<vector<int > >(2, vector<int>(3)));
        dp0[1][1][0]=1;
        dp0[1][0][1]=1;
        dp0[1][0][0]=1;
        int ans = 0;
        for(int i = 2; i<n+1; i++){
            // 对于Absence
            dp0[i][1][0] = 0;
            for(int k=0;k<3;k++){
                dp0[i][1][0]=(dp0[i-1][0][k]+dp0[i][1][0])%mod;
            }

            // 对于Late
            dp0[i][0][1] = dp0[i-1][0][0];
            dp0[i][1][1] = dp0[i-1][1][0];

            dp0[i][0][2] = dp0[i-1][0][1];
            dp0[i][1][2] = dp0[i-1][1][1];

            // 对于Presence
            dp0[i][0][0] = (dp0[i-1][0][1]+dp0[i-1][0][2])%mod;
            dp0[i][0][0] = (dp0[i][0][0]+dp0[i-1][0][0])%mod;

            dp0[i][1][0] = (dp0[i][1][0]+dp0[i-1][1][0])%mod;
            dp0[i][1][0] = (dp0[i][1][0]+dp0[i-1][1][1])%mod;
            dp0[i][1][0] = (dp0[i][1][0]+dp0[i-1][1][2])%mod;
        }
        for(int j=0;j<2;j++)
            for(int k=0;k<3;k++){
                ans = (ans+dp0[n][j][k])%mod;
            }
        return ans;
    }
};

int main()
{
    Solution sol;
    int n = 2;
    cout << sol.checkRecord(n) << endl;
    cout << sol.checkRecord(3) << endl;
    return 0;
}

// 12
// 1
// 1
// 123
// 1
//