#include <vector>
#include <iostream>
using std::vector;
using std::cin;
using std::cout;
using std::endl;

class Solution {
public:
    int findKthLargest(vector<int>&nums, int k) {
        quicksort(nums, 0, nums.size()-1);
        return nums[nums.size() - k];
    };


private:
    void quicksort(vector<int>&arr, int left, int right){
        int partition_index = right;
        if (left < right){
            partition_index = partition(arr, left, right);

            quicksort(arr, left, partition_index - 1);
            quicksort(arr, partition_index + 1, right);
        };
    };


    int partition(vector<int>&arr, int left, int right){
        int pivot = arr[right]; // Pivot is rightmost element.
        int partition_idx = left;

        for (int j = left; j<right; j++){
            if(arr[j]<pivot){
                swap(arr, partition_idx, j);
                partition_idx++;
            }
        };

        swap(arr, partition_idx, right);
        return partition_idx;
    };

    void swap(vector<int> &arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    };
};
