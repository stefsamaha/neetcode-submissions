class TimeMap:

    def __init__(self):
        self.store = {} # key = string, value = [ list of [str value, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" # in case key not in store 
        values = self.store.get(key, []) # gets value if key in dict, otherwise []

        # binary search 
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1 # we want to search in the right portion 
            
            else:
                r = m - 1 


        return res 




