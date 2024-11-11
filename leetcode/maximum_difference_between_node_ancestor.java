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
      return new int[]{0, Integer.MAX_VALUE, Integer.MIN_VALUE};
    }

    int[] left = dfs(node.left);
    int[] right = dfs(node.right);

    int min = Math.min(node.val, Math.min(left[1], right[1]));
    int max = Math.max(node.val, Math.max(left[2], right[2]));

    int ans = Integer.MIN_VALUE;
    if(node.left != null){
      ans = Math.max(left[0], Math.max(node.val - left[1], left[2] - node.val));
    }

    if(node.right != null){
      ans = Math.max(right[0], Math.max(node.val - right[1], right[2] - node.val));
    }

    return new int[]{ans, min, max};
  }

  public int maxAncestorDiff(TreeNode root){
    int[] result = dfs(root);
    return result[0];
  }
}
