/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */

// @lc code=start
/* 现实开发中更喜欢用这种方式，代码可读性很强，
 * 且性能与C++的方法差别不大
 */
class Solution {
    public int reverse(int x) {
        String xString = Integer.toString(x);
        String string = xString;
        int flag = 1;
        if (x < 0) {
            flag = -1;
            // 利用substring()获取子串，substring()中第一个参数是父串起始下标，第二个参数是父串结束下标
            string = xString.substring(1);
        }
        try {
            return Integer.valueOf((new StringBuilder(string)).reverse().toString()) * flag;
        }catch (Exception e){
            return 0;
        }
    }
}
// @lc code=end

