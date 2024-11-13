class Solution {
  public int rangeSumBST(TreeNode root, int low, int right){
    if(root == null){
      return 0;
    }

    int ans = 0;
    if (low <= root.val && root.val <= high){
      ans += root.val;
    }

    if (low < root.val){
      ans += rangeSumBST(root.left, low, high);
    }

    if(root.val < high){
      ans += rangeSumBST(root.right, low, high);
    }

    return ans;
  }
}
