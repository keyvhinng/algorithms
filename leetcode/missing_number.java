class Solution {
  
  public static void main(String[] args){
    Solution sol = new Solution();
    int[] numbers = {9,6,4,2,3,5,7,0,1};
    int res = sol.missingNumber(numbers);
    System.out.println(res);
  }

  public int missingNumber(int[] nums){
    int sum = 0;
    int n = nums.length;
    int total = (n*(n+1))/2;
    for(int i=0; i<n; i++){
      sum += nums[i];
    }
    return total - sum;
  }

}
