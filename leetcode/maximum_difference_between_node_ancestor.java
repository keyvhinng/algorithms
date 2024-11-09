class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode() {}
  TreeNode(int val) {this.val = val;}
  TreeNode(int val, TreeNode left, TreeNode right){
    this.val = val;
    this.left = left;
    this.right = right;
  }
}


class Solution {

  int[] dfs(TreeNode node){
    if(node == null){
      return new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
    }
    int[] left = dfs(node.left);
    int[] right = dfs(node.right);

    int min = Math.min(node.val, Math.min(left[0], right[0]));
    int max = Math.max(node.val, Math.max(left[1], right[1]));
    return new int[]{min, max};
  }

  public int maxAncestorDiff(TreeNode root){
    int[] result = dfs(root);
    return result[1] - result[0];
  }
}
