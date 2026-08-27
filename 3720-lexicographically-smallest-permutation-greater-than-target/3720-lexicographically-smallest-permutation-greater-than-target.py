class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = [0] * 26     # counts[c] = how many of letter c are left unused
        for ch in s:
            counts[ord(ch) - 97] += 1

        res = [''] * n   # final answer, built position by position
        stack = []       # positions where we "tied" with target (matched exactly)

        def smallest_greater(t_idx):
            # find smallest available letter strictly greater than letter t_idx
            for c in range(t_idx + 1, 26):
                if counts[c] > 0:
                    return c
            return -1

        def fill_ascending():
            # use up all remaining letters in sorted (smallest-first) order
            parts = []
            for c in range(26):
                if counts[c] > 0:
                    parts.append(chr(c + 97) * counts[c])
            return ''.join(parts)

        def backtrack():
            # undo ties one at a time, trying to diverge strictly greater at an earlier position
            while stack:
                j = stack.pop()
                tj_idx = ord(target[j]) - 97
                counts[tj_idx] += 1         # give back the letter used at j
                c_idx = smallest_greater(tj_idx)   # try strictly greater letter here instead
                if c_idx != -1:
                    counts[c_idx] -= 1
                    res[j] = chr(c_idx + 97)
                    return ''.join(res[:j + 1]) + fill_ascending()
                # else position j is also stuck -> keep popping further back
            return ""   # ran out of positions to backtrack -> no answer

        i = 0
        while i < n:
            t_idx = ord(target[i]) - 97

            if counts[t_idx] > 0:
                # tie: match target[i] exactly, remember this choice, move on
                counts[t_idx] -= 1
                res[i] = target[i]
                stack.append(i)
                i += 1
                continue

            # can't tie -> try to place a letter strictly greater than target[i]
            c_idx = smallest_greater(t_idx)
            if c_idx != -1:
                counts[c_idx] -= 1
                res[i] = chr(c_idx + 97)
                return ''.join(res[:i + 1]) + fill_ascending()

            # dead end here -> backtrack through previous ties
            return backtrack()

        # loop finished: res == target exactly, which is NOT strictly greater
        # -> must backtrack to find a strictly greater arrangement
        return backtrack()