class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;

        int res = 0;
        int ROWS = grid.size(), COLS = grid[0].size();

        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == 1) {
                    int tmp = dfs(r, c, grid, ROWS, COLS);
                    res = max(res, tmp);
                }
            }
        }
        return res;
    }

    int dfs(int row, int col, vector<vector<int>>& grid, int ROWS, int COLS){
        if (row < 0 || col < 0 || row >= ROWS || col >= COLS || grid[row][col] == 0){
            return 0;
        }

        grid[row][col] = 0;
        int area = 1;
        vector<pair<int, int>>dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};

        for (auto& [dr, dc] : dirs){
            int nr = row + dr, nc = col + dc;
            area += dfs(nr, nc, grid, ROWS, COLS);
        }
        return area;
    }
};