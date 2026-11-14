class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frec = {}
        for n in nums:
            frec[n] = 1 + frec.get(n,0)
        
        aux = []
        for n,f in frec.items():
            aux.append([f,n])
        aux.sort()

        res = []
        while len(res) < k:
            res.append(aux.pop()[1])

        return res
        