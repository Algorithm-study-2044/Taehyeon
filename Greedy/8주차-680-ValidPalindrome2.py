class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if (s[i] != s[-(i+1)]):
                return False
        return True
    def check(self, s: str) -> bool:
        if self.isPalindrome(s[1:]) or self.isPalindrome(s[:-1]):
            return True
        return False
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True  
        elif len(s) == 1 or len(s) == 2:
            return True
        else:
            if self.isPalindrome(s):
                return True
            else:
                start = 0
                end = len(s)-1
                while(start != len(s)-1):
                    if(s[start] != s[end]):
                        return self.check(s[start:end+1])
                    start += 1
                    end -= 1
            
        return False