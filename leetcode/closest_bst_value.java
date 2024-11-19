class Solution {
  int ans;

  
  void dfs(TreeNode node, double target){
    double diff1 = Math.abs(node.val-target);
    double diff2 = Math.abs(ans-target);
    if( (diff1<diff2) || (Double.compare(diff1,diff2)==0 && node.val<ans)){
      ans = node.val;
    }
    if(node.left != null){
      dfs(node.left,target);
    }
    if(node.right != null){
      dfs(node.right, target);
    }
  }

  public int closestValue(TreeNode root, double target){
    ans = root.val;
    dfs(root, target);
    return ans;
  }
}
