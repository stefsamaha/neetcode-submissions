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


# # You only care about when each car reaches the target, 
# not the actual movement over time. Arrival time = (target − position) / speed.

# # Sort cars by position descending so you process them from closest to the target → farthest.
# # → This way, every car only needs to compare itself to the car/fleet ahead.

# # A car can only merge with the fleet directly in front of it, 
# since it cannot pass cars.

# # If a car behind has an arrival time ≤ the arrival time of the fleet ahead, 
# it will eventually catch up, so it becomes part of that fleet.

# # If a car behind has an arrival time > the fleet ahead, 
# it can never catch up before reaching the target → it forms a new fleet.

# # Maintain only one variable, curtime, representing the arrival time of the last fleet formed.
# # → This acts like a “stack top” without needing a full stack.

# # Every time dest_time > curtime, that car starts a new fleet, 
# and we update curtime.

# # The total number of times this happens = number of fleets.