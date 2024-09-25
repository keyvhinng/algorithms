import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;


class Solution {
    public List<List<Integer>> findWinners(int[][] matches){
        List<List<Integer>> result = new ArrayList<>();

        List<Integer> zeroLoss = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();
        Set<Integer> winners = new HashSet<>();
        Set<Integer> losers = new HashSet<>();
        HashMap<Integer, Integer> losses = new HashMap<>();

        for(int[] match: matches){
            int winner = match[0];
            int loser = match[1];

            winners.add(winner);
            losers.add(loser);

            losses.put(loser, losses.getOrDefault(loser, 0) + 1);
        }

        for(int player: winners){
            if(!losers.contains(player)){
                zeroLoss.add(player);
            }
        }

        for(int player: losses.keySet()){
            if(losses.get(player) == 1){
                oneLoss.add(player);
            }
        }

        Collections.sort(zeroLoss);
        Collections.sort(oneLoss);

        result.add(zeroLoss);
        result.add(oneLoss);
        return result;
    }
}