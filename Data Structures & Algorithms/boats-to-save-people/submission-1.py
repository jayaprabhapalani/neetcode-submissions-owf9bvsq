class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # from lightest to heaviest
        l=0
        r=len(people)-1
        boats=0

        while l<=r:
            # if lightest and heaviest person can travel in a same baot
            if people[l]+people[r]<=limit: 
                l+=1
            #if not then heaviest person has to travel alone 
            #and increase the boat cnt
            r-=1
            boats+=1
        return boats         
        