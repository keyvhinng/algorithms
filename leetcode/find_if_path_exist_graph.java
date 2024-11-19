class Solution {
  public boolean validPath(int n, int[][] edges, int source, int destination){
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

    seen.add(source);
    boolean res = dfs(source,destination,graph,seen);

    return false;
  }

  boolean dfs(int current, int destination, ArrayList<ArrayList<Integer>> graph, Set<Integer> seen){
    if(current==destination){
      return true;
    }

    
    for(int i=0; i<graph.get(current).size(); i++){
      int v = graph.get(current).get(i);
      if (!seen.contains(v)){
        seen.add(v);
        if(dfs(v, destination, graph, seen)){
          return true;
        }
      }
    }

    return false;
  }
}
