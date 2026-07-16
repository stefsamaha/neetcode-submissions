class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleets = curtime = 0

        for dist, speed in sorted(pairs, reverse=True):
            dest_time = (target-dist)/speed 
            if dest_time > curtime:
                fleets +=1
                curtime = dest_time
        
        return fleets 


        