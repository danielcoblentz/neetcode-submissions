class Solution {
public:
    int dfs(int row, int col, int ROWS, int COLS, vector<vector<int>>& grid) {
        if (row < 0 || row >= ROWS || col < 0 || col >= COLS || grid[row][col] == 0) return 0;
        grid[row][col] = 0;
        int area = 1;
        vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        for (auto& [dr, dc] : dirs) {
            int newR = row + dr, newC = col + dc;
            area += dfs(newR, newC, ROWS, COLS, grid);
        }
        return area;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;

        int ROWS = grid.size(), COLS = grid[0].size();
        int res = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    int tmp = dfs(r, c, ROWS, COLS, grid);
                    res = max(res, tmp);
                }
            }
        }
        return res;
    }
};