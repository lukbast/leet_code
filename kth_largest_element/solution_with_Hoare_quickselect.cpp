#include <vector>
#include <iostream>
using std::vector;
using std::cin;
using std::cout;
using std::endl;

class Solution {
public:
    int findKthLargest(vector<int>&nums, int k) {
        int idx = nums.size() -k;
        
        return quickselect(nums, 0, nums.size()-1, idx);
    };


private:
    int quickselect(vector<int>&arr, int left, int right, int idx_to_find){
        int partition_index = partition(arr, left, right);
        if (partition_index == idx_to_find){
            return arr[partition_index];
        } else if (idx_to_find < partition_index) {
            return quickselect(arr, left, partition_index -1, idx_to_find);
        } else {
            return quickselect(arr, partition_index +1, right, idx_to_find);
        }

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

int main(){
    vector<int> numbers = {6, 3, 9, 2, 0, 4, 5, 7};
    Solution sol = Solution();
    int idx = sol.findKthLargest(numbers, 3);
    for (auto const &i: numbers) {
        cout << i << " ";
    };
    cout << endl;
    cout << idx << endl;

    return 0;
};
