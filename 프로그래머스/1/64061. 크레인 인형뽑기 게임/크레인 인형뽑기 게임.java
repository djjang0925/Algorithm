import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<Integer>();
        int length = board[0].length;
        int answer = 0;
        
        for (int i = 0; i < moves.length; i++) {
            int now = moves[i] - 1;
            
            if (stack.isEmpty()) {
                for (int j = 0; j < length; j++) {
                    if (board[j][now] != 0) {
                        stack.push(board[j][now]);
                        board[j][now] = 0;
                        break;
                    }
                }
            } else {
                for (int j = 0; j < length; j++) {
                    if (board[j][now] != 0) {
                        if (board[j][now] == stack.lastElement()) {
                            answer+=2;
                            stack.pop();
                            board[j][now] = 0;
                        } else {
                            stack.push(board[j][now]);
                            board[j][now] = 0;
                        }
                        
                        break;
                    }
                }
            }
        }
        return answer;
    }
}