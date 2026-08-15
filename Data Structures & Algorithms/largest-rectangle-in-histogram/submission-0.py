class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #intution---> height[i]*width
        #width=right_bound-left_bound-1
        #right boundary=next smallest element index
        #left boundary=previous smallest element index
        #needed things- stack,max_area var,left and right arr boundary( left with -1 and right with n(len)) , the one loop to calculate the max
        #so t.c is O(3n)
        n=len(heights)
        stack=[]
        max_area=0
        left=[-1]*n
        right=[n]*n

        #prev smallest index--- left boundary
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            left[i]=stack[-1] if stack else -1
            stack.append(i)#update the curr index in stack
        
        stack=[]
        #next smallest index -- right boundary
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            right[i]=stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            area=heights[i]*(right[i]-left[i]-1)
            max_area=max(max_area,area)
        
        return max_area



        