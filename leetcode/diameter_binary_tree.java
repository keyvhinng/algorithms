class Solution {

  int diameter;

  int dfs(TreeNode node){
    int left_max_depth = 0;
    int right_max_depth = 0;
    if (node.left != null){
      left_max_depth = dfs(node.left);
    }

    if (node.right != null){
      right_max_depth = dfs(node.right);
    }

    int max_depth = Math.max(left_max_depth, right_max_depth);

    int curr_sol = left_max_depth + right_max_depth;
    diameter = Math.max(diameter, curr_sol);
    
    return 1 + max_depth;
  }

  public int diameterOfBinaryTree(TreeNode root){
    diameter = 0;
    dfs(root);
    return sol;
  }

}
