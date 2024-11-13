class Solution {
  public int getMinimumDifference(TreeNode root){
    List<Integer> values = new ArrayList<>();
    dfs(root, values);
    int ans = Integer.MAX_VALUE;
    for(int i=1; i<values.size(); i++){
      ans = Math.min(ans, values.get(i) - values.get(i-1));
    }
    return ans;
  }

  public void dsf(TreeNode node, List<Integer> values){
    if(node==null){
      return;
    }
    dfs(node.left, values);
    values.add(node.val);
    dfs(node.right, values);
  }
}
