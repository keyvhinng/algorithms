class Solution {
  public List<List<Integer>> zigzagLevelOrder(TreeNode root){
    if(root == null){
      return new ArrayList<>();
    }

    List<List<Integer>> ans = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    int direction = 0;

    while(!queue.isEmpty()){
      int currentLength = queue.size();
      List<Integer> currentLevel = new ArrayList<>();
      for(int i=0 ; i<currentLength; i++){
        TreeNode node = queue.remove();
        currentLevel.add(node.val);

        if(node.left != null){
          queue.add(node.left);
        }

        if(node.right != null){
          queue.add(node.right);
        }
      }

      if(direction == 1){
        Collections.reverse(currentLevel);
      }

      ans.add(currentLevel);
      direction = 1 - direction;
    }

    return ans;
  }
}
