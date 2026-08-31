class Solution {
public:
    int ROWS, COLS;
    void dfs(int r, int c, vector<vector<char>>& grid){
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || grid[r][c] == '0') return;
        grid[r][c] = '0';
        vector<pair<int,int>> dirs = {{1,0},{0,1},{-1,0},{0,-1}};
        for (auto& dir : dirs){
            dfs(r + dir.first, c + dir.second, grid);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        ROWS = grid.size(); COLS = grid[0].size();
        int res = 0;
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == '1'){
                    res++;
                    dfs(r, c, grid);
                }
            }
        }
        return res;
    }
};