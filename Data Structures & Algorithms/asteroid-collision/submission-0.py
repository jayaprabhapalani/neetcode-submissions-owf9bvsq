class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            if stack and asteroids[i]<0:
            #when both are same
                if stack and stack[-1]== -asteroids[i]:
                    stack.pop()
            #when +ve < -ve        
                while stack and stack[-1]<-asteroids[i]:
                    stack.pop()
                stack.append(asteroids[i])
            #when +ve> -ve
                if stack and stack[-1]>asteroids[i]:
                    break
            else:
                stack.append(asteroids[i])
        return stack
            

            

            

        