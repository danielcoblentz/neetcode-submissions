class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        if (!grid.size() || !grid[0].size()) return;

        int ROWS = grid.size(), COLS = grid[0].size();
        queue<pair<int,int>>q;
        int INF = 2147483647;
        vector<pair<int, int>> dirs = {{1,0}, {0, 1}, {-1,0},{0,-1}};
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == 0){
                    q.push({r, c});
                }
            }
        }

        while (q.size()){
            //get node
            int row = q.front().first, col = q.front().second;
            q.pop();

            for (auto& [dr, dc] : dirs) {
                int newR = dr + row, newC = dc + col;
                if (min(newR, newC) < 0 || newR == ROWS || newC == COLS || grid[newR][newC] != INF) continue;

                grid[newR][newC] = grid[row][col] + 1;
                q.push({newR, newC});

            }



        }
    }
};
