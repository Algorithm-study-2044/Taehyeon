class Solution:
    M = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(1000):
        M[i][i] = 1

    def longestPalindrome(self, s: str) -> str:
        Solution.M = [[0 for i in range(1000)] for j in range(1000)]
        for i in range(1000):
            Solution.M[i][i] = 1
        ans = 1; fr = 0; to = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                Solution.M[i][i+1] = 1
                ans = 2; fr = i; to = i+1
        for i in range(len(s)-3, -1, -1):
            for j in range(i+2, len(s)):
                if Solution.M[i+1][j-1] and (s[i] == s[j]):
                    Solution.M[i][j] = 1
                    if j - i + 1 > ans:
                        ans = j - i + 1; fr = i; to = j
        return s[fr:to+1]
        
        
        