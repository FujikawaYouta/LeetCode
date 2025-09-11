#include <iostream>
using namespace std;
class Solution {
public:
    int findPos(vector<int>&nums, int l, int r) {
        srand(time(0));
        int i = rand()%(r-l+1)+l; // 随机选一个作为我们的主元
        int target = nums[i];
        swap(nums[l],nums[i]);
        while(l<r){
            while(l<r && nums[r]>=target) r--;
            nums[l]=nums[r];
            while(l<r && nums[l]<=target) l++;
            nums[r]=nums[l];
        }
        nums[l]=target;
        return l;
    }
    void quickSort(vector<int>& nums, int l, int r) {
        if(l<r){
            int correctPos = findPos(nums, l, r);
            quickSort(nums, l, correctPos-1);
            quickSort(nums, correctPos+1, r);
        }
    }
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size()-1);
        return nums;
    }
};
int main()
{
    Solution sol;
    vector<int> nums = {49,38,65,97,76,13,27,49};
    // vector<int> nums = {110,100,0};
    nums = sol.sortArray(nums);
    return 0;
}