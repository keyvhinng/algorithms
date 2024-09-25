import java.util.HashSet;
import java.util.Set;

class Solution {

  public static void main(String[] args){
    Solution sol = new Solution();
    int[] arr = {1,1,3,3,5,5,7,7};
    int res = sol.countElements(arr);
    System.out.println(res);
  }

  public int countElements(int[] arr){
    int ans = 0;
    Set<Integer> intSet = new HashSet<>();
    for(int i=0; i<arr.length; i++){
      intSet.add(arr[i]);
    }
    for(int i=0; i<arr.length; i++){
      if(intSet.contains(arr[i]+1)){
        ans++;
      }
    }
    return ans;
  }
}
