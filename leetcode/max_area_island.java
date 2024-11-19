class Solution {
  int[] dx = { 0, -1, 0, 1};
  int[] dy = {-1,  0, 1, 0};

  public int maxAreaOfIsland(int[][] grid){
    int n = grid.length;
    int m = grid[0].length;
    int ans = 0;

    for(int i=0; i<n; i++){
      for(int j=0; j<m; j++){
        if(grid[i][j]==1){
          ans = Math.max(ans, dfs(i,j,n,m,grid));
        }
      }
    }

    return ans;
  }

  int dfs(int x, int y, int n, int m, int[][] grid){
    int ans = 1;
    grid[x][y]=0;
    for(int i=0; i<4; i++){
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(isValid(nx, ny, n, m, grid)){
        ans += dfs(nx,ny,n,m,grid);
      }
    }
    return ans;
  }

  boolean isValid(int x, int y, int n, int m, int[][] grid){
    if(x>=0 && x<n && y>=0 && y<m && grid[x][y]==1){
      return true;
    }
    return false;
  }
}
