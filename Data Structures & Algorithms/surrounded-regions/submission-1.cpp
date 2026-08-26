class Solution {
public:
    void dfs(vector<vector<char>>& board, int r, int c) {
        if (r < 0 || c < 0 || r >= board.size() || c >= board[0].size() || board[r][c] != 'O') return;
        board[r][c] = '#';
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }

    void solve(vector<vector<char>>& board) {
       if (board.empty() || board[0].empty()) return;

       int ROWS = board.size(), COLS = board[0].size();

       for (int i = 0; i < ROWS; i++) {
           dfs(board, i, 0);
           dfs(board, i, COLS - 1);
       }
       for (int j = 0; j < COLS; j++) {
           dfs(board, 0, j);
           dfs(board, ROWS - 1, j);
       }

       for (int row = 0; row < ROWS; row++){
        for (int col = 0; col < COLS; col++){
            if (board[row][col] == 'O') board[row][col] = 'X';
            if (board[row][col] == '#') board[row][col] = 'O';
        }
       } 
    }
};