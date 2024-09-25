import java.util.HashMap;

class Solution {
  public int largestUniqueNumber(int[] nums){
    HashMap<Integer, Integer> count = new HashMap<>();   
    for(int num: nums){
      count.put(num, count.getOrDefault(num,0));
    }

    int largest = -1;
    for(int num: count.keySet()){
      if(count.get(num) == 1){
        largest = Math.max(largest, num);
      }
    }
    return largest;
  }
}
