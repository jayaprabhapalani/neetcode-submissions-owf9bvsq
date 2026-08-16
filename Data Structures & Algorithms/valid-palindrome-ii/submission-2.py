class Solution:
    def validPalindrome(self, s: str) -> bool:
        # normal palindrom func
        def palindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        # now our curr task is - so the given word may have one extra char that makes the word not palindrome , we just need to ingnore that and perform palindrom check
        # now that word can either in the left ptr or right ptr - so we are skipping that and giving the chars for palindrome check
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return palindrome(l+1,r) or palindrome(l,r-1)
            l+=1
            r-=1
        return True