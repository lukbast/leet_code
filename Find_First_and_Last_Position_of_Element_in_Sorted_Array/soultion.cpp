#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0){
            return vector<int> {-1, -1};
        }
        int first_pos = binary_search(target, nums);
        if (first_pos == -1){
            return vector<int> {-1, -1};
        }
        
    }
    private:
    int binary_search(int value_to_find, vector<int> &arr){
    int left = 0;
    int right = arr.size();
    int mid;

    while (left < right){
        mid = (left + right) / 2;
        int found_value = arr[mid];
        if(found_value == value_to_find){
            return mid;
        } else if (found_value < value_to_find){
            left = mid +1;
        } else {
            right = mid -1; 
        }
    }

    if (arr[left] == value_to_find){
        return left;
    } else {
        return -1;
    }
    
}
};
