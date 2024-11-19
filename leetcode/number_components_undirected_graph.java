class Solution {
  public int countComponents(int n, int[][] edges){
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    Set<Integer> seen = new HashSet<>();

    for(int i=0; i<n; i++){
      graph.add(new ArrayList<>());
    }

    for(int i=0; i<edges.length; i++){
      int u = edges[i][0];
      int v = edges[i][1];
      graph.get(u).add(v);
      graph.get(v).add(u);
    }

    int ans = 0;

    for(int i=0; i<n; i++){
      if(!seen.contains(i)){
        ans++;
        seen.add(i);
        dfs(i, graph, seen);
      }
    }

    return ans;
  }

  void dfs(int current, ArrayList<ArrayList<Integer>> graph, Set<Integer> seen){
    for(int i=0; i<graph.get(current).size(); i++){
      int v = graph.get(current).get(i);
      if(!seen.contains(v)){
        seen.add(v);
        dfs(v, graph, seen);
      }
    }
    return;
  }
}
