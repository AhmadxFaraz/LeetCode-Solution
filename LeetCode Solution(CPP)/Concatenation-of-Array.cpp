#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> nums1 = nums;
        vector<int> final = nums1;
        final.insert(final.end(), nums.begin(), nums.end());
        return final;
    }
};