class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(',']':'[','}':'{'}
        #closing tag as keys opening tag as value
        #to match the tags
        for ch in s:
            #opening tags
            if ch in mapping.values():
                stack.append(ch)
            #closing tags        
            else:
                # stack is empty or not match -- false
                if not stack or mapping[ch]!=stack[-1]:
                    return False
                else:
                    stack.pop()  
        return not stack          


        