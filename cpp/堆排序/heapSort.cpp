#include<iostream>
using namespace std;

void HeapAdjust(vector<int>& arr, int len, int curIdx) {
    arr[0] = arr[curIdx]; //临时存储待换元素
    for(int i=2*curIdx;i<=len;i*=2) { //左孩子结点
        if(arr[i]<arr[i+1]) i++;
        if(arr[0]>arr[i]) break;
        else {
            arr[curIdx] = arr[i];
            curIdx = i; //指定位置变为i
        }
    }
    arr[curIdx] = arr[0]; //待换元素换到指定位置
}
void BuildMaxHeap(vector<int>& arr, int len) {
    for (int i=len/2;i>0;i--){
        HeapAdjust(arr, len, i);
    }
}
int main()
{
    vector<int> arr = {0,53,17,78,9,45,65,87,32};
    BuildMaxHeap(arr, 8);
    return 0;
}