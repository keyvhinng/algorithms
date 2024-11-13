class Solution {
  public TreeNode insertIntoBST(TreeNode root, int val){
    TreeNode newNode = new TreeNode(val);
    if(root==null){
      return newNode;
    }

    dfs(root, newNode);
    return root;
  }

  void dfs(TreeNode node, TreeNode newNode){
    if(newNode.val < node.val){
      if(node.left == null){
        node.left = newNode;
      }else{
        dfs(node.left, newNode);
      }
    }else{
      if(node.right == null){
        node.right = newNode;
      }else{
        dfs(node.right, newNode);
      }
    }
  }
}
