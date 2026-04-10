class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op=[]
        a,b=0,0
        while a<len(word1) and b<len(word2):
            op.append(word1[a])
            op.append(word2[b])
            a+=1
            b+=1
        op.append(word1[a:]) or op.append(word2[b:])

        return "".join(op)      




        