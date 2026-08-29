class UF:
    def __init__(self, nums, limit):
       
        self.par = {x: x for x in nums}
        self.limit = limit
        
    def find(self, x):
        if self.par[x] != x: 
            self.par[x] = self.find(self.par[x])
        return self.par[x]
        
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb and abs(a - b) <= self.limit: 
            self.par[pa] = pb 

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        uf = UF(nums, limit) 
        s = sorted(nums)

        for i in range(1, n): 
            uf.union(s[i-1], s[i])
            
        comp_sl = defaultdict(SortedList)
        res = [0] * n
        
        for i, x in enumerate(nums):
            c = uf.find(x)
            res[i] = c 
            comp_sl[c].add(x)
        
        for i, c in enumerate(res):
            res[i] = comp_sl[c].pop(0)

        return res