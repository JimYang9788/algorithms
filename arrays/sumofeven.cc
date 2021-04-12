class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        vector <int> ::iterator it;
        int res = 0;
        for (int i = 0; i < arr.size() / 2 +1; i ++){
            int length = 2 * i + 1; 
            for (int start = 0; start < arr.size() - length + 1; start ++){
                for (int j = start; j < start + length; j ++){
                    res += arr[j];
                }    
            }
        }
        return res;
    }
};