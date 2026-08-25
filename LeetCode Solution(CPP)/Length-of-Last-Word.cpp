#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        //soltuion to problem 58, length of last word
        int length = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                length++;
            } else if (length > 0) {
                break;
            }
        }
        return length;
    }
};