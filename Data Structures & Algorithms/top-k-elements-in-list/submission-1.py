class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create a hashmap (dictionary)
        freq = [[] for x in range (len(nums)+1)] #a list the size of nums, each entry's index is its freq in nums 

        for x in nums:
            count[x] = 1 + count.get(x, 0) #key + the default 0 if unseen 

        for n, c in count.items():
            freq[c].append(n) # we're saying that n occurs c number of times 

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res 

# O(n) better than O(klogn) using a maxheap



         


        