/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution {
public:
    int reverse(int x) {
        long n = 0;
        while(x){
            n = n * 10 + x % 10;
            x = x / 10;
        }
        return n > INT_MAX || n < INT_MIN ? 0 : n;
        // return int(n) == n ? int(n) : 0;
    }
};
// @lc code=end

