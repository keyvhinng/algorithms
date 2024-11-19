class Solution {
  int ans;

  public int reachableNodes(int n, int[][] edges, int[] restricted){
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    Set<Integer> seen = new HashSet<>();
    Set<Integer> restrictedSet = new HashSet<>();

    for(int i=0; i<n; i++){
      graph.add(new ArrayList<>());
    }

    for(int i=0; i<restricted.length; i++){
      restrictedSet.add(restricted[i]);
    }

    for(int i=0; i<edges.length; i++){
      int u = edges[i][0];
      int v = edges[i][1];
      graph.get(u).add(v);
      graph.get(v).add(u);
    }

    seen.add(0);
    ans = dfs(0,graph, seen, restrictedSet);
    return ans;
  }

  int dfs(int node, ArrayList<ArrayList<Integer>> graph, Set<Integer> seen, Set<Integer> restrictedSet){
    int ans = 1;
    for(int i=0; i<graph.get(node).size(); i++){
      int v = graph.get(node).get(i);
      if(!seen.contains(v) && !restrictedSet.contains(v)){
        seen.add(v);
        ans += dfs(v, graph, seen, restrictedSet);
      }
    }
    return ans;
  }
}
