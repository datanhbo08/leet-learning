class Solution:

  def minimumDeletions(self, nums: List[int]) -> int:
    n = len(nums) # Total length of the array
    mn, mx = nums.index(min(nums)), nums.index(max(nums)) # Find indices of the minimum and maximum elements
    l, r = min(mn, mx), max(mx, mn) # Identify the left-most and right-most positions between min and max


    return min(r + 1, n - l, l + 1 + n - r)
    # Min deletions: remove both from left, both from right, or one from each side