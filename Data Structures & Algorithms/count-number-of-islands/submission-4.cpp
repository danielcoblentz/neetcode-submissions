class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int res = 0;

        int ROWS = grid.size(), COLS = grid[0].size();

        for (int row = 0; row < ROWS; row++){
            for (int col = 0; col < COLS; col++){
                if (grid[row][col] == '1') {
                    res++;
                    dfs(row, col, grid);
                }

            }
        }
        return res;
    }

    void dfs(int row, int col, vector<vector<char>>& grid){
        int ROWS = grid.size(), COLS = grid[0].size();
        if (row < 0 || col < 0 || row >= ROWS || col >= COLS || grid[row][col] == '0') return;
        
        grid[row][col] = '0';
        vector<pair<int, int>> dirs = {{0,1}, {1,0}, {-1,0}, {0, -1}};

        for (auto [dr, dc] : dirs){
            int nr = row + dr, nc = col + dc;
            dfs(nr, nc, grid);
        }
    }
};
