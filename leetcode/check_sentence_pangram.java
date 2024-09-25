import java.util.HashSet;
import java.util.Set;

class Solution {
  public static void main(String[] args){
    Solution sol = new Solution();
    boolean res = sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"); 
    System.out.println(res);
  }

  public boolean checkIfPangram(String sentence){
    Set<Character> charSet = new HashSet<>();

    for(int i=0; i<sentence.length(); i++){
      charSet.add(sentence.charAt(i));
    }

    int size = charSet.size();

    return size == 26;
  }
}
