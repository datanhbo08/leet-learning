class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)              # Length of string
        res = ''                # Stores the best result
        o = 0                   # Count of '1's in current window
        l = 0                   # Left pointer of the window

        # Expands the window to the right by moving 'r'
        for r in range(n):
            if s[r] == '1': 
                o += 1          # Increment count if we see '1'
            
            # Shrinks the window from the left to remove excess '1's or leading '0's
            while l <= r and (o > k or s[l] == '0'):
                if s[l] == '1': 
                    o -= 1
                l += 1          
                
            # If window has exactly k '1's, check if it's the best option
            if o == k:
                ss = s[l : r + 1] # Current candidate substring
                if not res or len(ss) < len(res) or (len(ss) == len(res) and ss < res):
                    res = ss
                    
        return res