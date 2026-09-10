class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start by assuming the whole first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix against every other string
        for s in strs[1:]:
            # Shrink the prefix from the end until s starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""  # No common prefix left
        
        return prefix