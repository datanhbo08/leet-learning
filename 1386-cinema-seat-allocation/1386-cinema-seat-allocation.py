class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        res = 0
        mp = defaultdict(set)
        for r, c in reservedSeats:
            mp[r].add(c) 

        seenr = 0
        for k in mp:
            seenr += 1
            valid1 = all(j not in mp[k] for j in range(2, 6))   
            valid2 = all(j not in mp[k] for j in range(4, 8))   
            valid3 = all(j not in mp[k] for j in range(6, 10)) 

            res += max(valid2, valid1 + valid3)

        return res + (n - seenr) * 2