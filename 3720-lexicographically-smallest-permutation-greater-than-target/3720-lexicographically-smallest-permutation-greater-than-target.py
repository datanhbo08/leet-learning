class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)                  # Length of the source string
        fm = defaultdict(int)       # Frequency map of characters in s
        for c in s: 
            fm[c] += 1
        res = []                    # Prefix result list

        for ti in range(n):         # Iterate through each character index of target
            t = target[ti]          # Current character of target
            if fm[t] > 0:           # If character is available in frequency map
                fm[t] -= 1          # Use the character temporarily
                largest = []        # Build the largest possible suffix with remaining chars
                for ci in range(25, -1, -1):
                    c = chr(ci + ord('a'))
                    if fm[c] > 0: 
                        largest.append(c * fm[c])

                # If remaining largest string exceeds target suffix, lock character in
                if "".join(largest) > target[ti + 1:]: 
                    res.append(t)
                    continue
                fm[t] += 1          # Backtrack if it doesn't satisfy the condition
            
            # Find the next strictly greater character than t to diverge
            for nti in range(ord(t) - ord('a') + 1, 26):
                c = chr(nti + ord('a'))
                if fm[c] > 0: 
                    res.append(c)
                    fm[c] -= 1 
                    smallest = []   # Build the smallest possible suffix to minimize result
                    for ci in range(26):
                        c = chr(ci + ord('a'))
                        if fm[c] > 0:
                            smallest.append(c * fm[c]) 
                    return "".join(res + smallest)
            return ""
        return ""