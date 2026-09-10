class Solution:

  def averageOfSubtree(self, root: TreeNode) -> int:
    self.res = 0  # Stores the count of valid nodes

    def dfs(node):
      if not node:
        return 0, 0  # Base case: empty node has sum 0 and count 0

      # Recursively get (sum, count) from left and right subtrees
      lval, lcount = dfs(node.left)
      rval, rcount = dfs(node.right)

      # Total sum and node count for the current subtree
      nval, ncount = lval + rval + node.val, lcount + rcount + 1

      # Increment result if the subtree average equals the node's value
      if nval // ncount == node.val:
        self.res += 1
      return nval, ncount

    dfs(root)
    return self.res