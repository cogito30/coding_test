// 카카오프렌즈 컬러링북
import java.util.*;

class Solution {
    
    static class Position {
        public int x;
        public int y;
        
        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public int bfs(int[][] board, int row, int col) {
        int currentAreaSize = 0;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        int color = board[row][col];
        
        Queue<Position> queue = new LinkedList<Position>();
        
        queue.offer(new Position(row, col));
        board[row][col] = 0;
        currentAreaSize++;
        
        while (queue.size() > 0) {
            row = queue.peek().x;
            col = queue.peek().y;
            queue.poll();
        
            for (int i = 0; i < 4; ++i) {
                int nr = row + dr[i];
                int nc = col + dc[i];

                if (nr < 0 || nr >= board.length || nc < 0 || nc >= board[0].length)
                    continue;

                if (board[nr][nc] != 0 && board[nr][nc] == color) {
                    queue.offer(new Position(nr, nc));
                    board[nr][nc] = 0;
                    currentAreaSize++;
                }
            }
        }
        return currentAreaSize;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int currentSizeOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < n; ++col) {
                if (picture[row][col] != 0) {
                    
                    currentSizeOfArea = bfs(picture, row, col);
                    numberOfArea++;
                    System.out.println(row + " " + col + " " + currentSizeOfArea);
                    if (currentSizeOfArea > maxSizeOfOneArea) {
                        maxSizeOfOneArea = currentSizeOfArea;
                    }
                }
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
}