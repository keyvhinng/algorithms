class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode() {}

  TreeNode(int val) {
    this.val = val;
  }

  TreeNode(int val, TreeNode left, TreeNode right){
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class Solution {

  int dfs(TreeNode node, int currDepth){
    if(node.left==null && node.right==null){
      return currDepth;
    }

    int leftDepth = Integer.MAX_VALUE;
    int rightDepth = Integer.MAX_VALUE;

    if(node.left!=null){
      leftDepth = dfs(node.left,1+currDepth);
    }

    if(node.right!=null){
      rightDepth = dfs(node.right,1+currDepth);
    }

    return Math.min(leftDepth, rightDepth);
  }

  public int minDepth(TreeNode root){
    if(root==null) return 0;
    return dfs(root, 1);
  }
}
