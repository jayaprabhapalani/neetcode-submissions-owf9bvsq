class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f_s={}
        f_t={}
        for i in s:
            f_s[i]=f_s.get(i,0)+1
        for i in t:
            f_t[i]=f_t.get(i,0)+1

        if f_s==f_t:
            return True
        return False        


        