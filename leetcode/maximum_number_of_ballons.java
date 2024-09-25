class Solution {
  public int maxNumberOfBallons(String text){
    HashMap<Character, Integer> count = new HashMap<>();
    for(int i=0; i<text.length(); i++){
      char c = text.charAt(i);
      count.put(c, count.getOrDefault(c,0)+1);
    }
    int res = 10000;
    res = Math.min(res, count.getOrDefault('b',0));
    res = Math.min(res, count.getOrDefault('a',0));
    res = Math.min(res, count.getOrDefault('l',0) / 2);
    res = Math.min(res, count.getOrDefault('o',0));
    res = Math.min(res, count.getOrDefault('n',0));

    return res;
  }
}
