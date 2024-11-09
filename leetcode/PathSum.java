class PathSum {
  int target;

  public boolean hasPathSum(TreeNode root, int targetSum){
    target = targetSum;
    return dfs(root, 0);
  }

  public boolean dfs(TreeNode node, int curr){'
    if (node == null){
      return False;
    }

    if (node.left == null && node.right == null){
      return (curr + node.val) == target;
    }

    curr += node.val;
    boolean left  = dfs(node.left, curr);
    boolean right = dfs(node.right, curr); 
    return left || right;
  }
}
