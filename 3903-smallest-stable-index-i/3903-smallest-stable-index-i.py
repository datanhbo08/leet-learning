class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = [0] * n   # prefix_max[i] = max(nums[0..i])
        suffix_min = [0] * n   # suffix_min[i] = min(nums[i..n-1])

        # Build prefix max: running max from the left
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # Build suffix min: running min from the right
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Check each index left to right; first one with score <= k wins
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i

        return -1