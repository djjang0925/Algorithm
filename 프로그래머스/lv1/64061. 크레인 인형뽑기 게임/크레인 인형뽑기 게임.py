def solution(board, moves):
    stack = []
    ans = 0
    
    for i in range(len(moves)):
        grab = 0
        x = moves[i] - 1
        
        for j in range(len(board)):
            if board[j][x] != 0:
                grab = board[j][x]
                board[j][x] = 0
        
                if not stack:
                    stack.append(grab)
                elif stack[-1] == grab:
                        stack.pop()
                        ans += 2
                else:
                    stack.append(grab)
                
                break
                    
                    
    return ans
