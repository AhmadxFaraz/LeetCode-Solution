class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]==0){
                count++;
            }
        }
        erase(nums, 0);
        vector<int> arr;
        arr.resize(count,0);
        nums.insert(nums.end(), arr.begin(), arr.end());
        return nums;
    }
};