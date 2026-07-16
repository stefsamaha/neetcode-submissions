class Solution:
    def isPalindrome(self, s: str) -> bool:
        #INEFFICIENT WITH O(N) SPACE

        result = ""
        for x in s:
            if x.isalnum():
                result+=x.lower()
        
        return result == result[::-1]