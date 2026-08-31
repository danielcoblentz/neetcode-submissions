class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int res = 0;
        vector<pair<int, int>> dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        queue<pair<int, int>> q;
        int ROWS = grid.size(), COLS = grid[0].size();
        int time = 0;
        //seed da q
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == 2) q.push({r,c});
                if (grid[r][c] == 1) res ++;
            }
        }

        while (q.size() && res > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int row = q.front().first, col = q.front().second;
                q.pop();

                for (auto& [dr, dc] : dirs) {
                    int newR = dr + row, newC = dc + col;

                    if (min(newR, newC) < 0 || newR == ROWS || newC == COLS || grid[newR][newC] != 1) continue;
                    grid[newR][newC] = 2;
                    q.push({newR, newC});
                    res --;
                }
            }
            time ++;
        }

        return res == 0 ? time : -1;
    }
};