class Solution {
  public int deepestLeavesSum(TreeNode root){
    if(root==null){
      return -1;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    int level = 0;
    int ans = 0;

    while(!queue.isEmpty()){
      int currentLength = queue.size();
      int currSum = 0;
      for(int i=0; i<currentLength; i++){
        TreeNode node = queue.remove(); 
        currSum += node.val;
        
        if(node.left != null){
          queue.add(node.left);
        }

        if(node.right != null){
          queue.add(node.right);
        }
      }

      ans = currSum;

      level++;
    }

    return ans;
  }
}
