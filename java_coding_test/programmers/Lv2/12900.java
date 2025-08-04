// 2 x n 타일링
class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 2;
        
        for (int i = 0; i < n - 2; ++i) {
            dp[i+2] = (dp[i] + dp[i+1]) % 1_000_000_007;
        }
        answer = dp[n-1];
        return answer;
    }
}