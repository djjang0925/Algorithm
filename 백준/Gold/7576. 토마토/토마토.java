import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[][] Graph;
    static int[][] Used;
    static int[] My = {1 , -1, 0, 0};
    static int[] Mx = {0, 0, 1 , -1};
    static Deque<int[]> deque = new ArrayDeque<>();
    static int Left = 0;
    static int Days = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        Graph = new int[N][M];
        Used = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j< M; j++) {
                int n = Integer.parseInt(st.nextToken());
                Graph[i][j] = n;

                if (n == 1) {
                    deque.addLast(new int[]{i, j});
                    Used[i][j] = 1;
                    Left++;
                }
            }
        }

        Bfs();

        for (int[] i : Graph) {
            for (int j : i) {
                if (j == 0) {
                    System.out.println(-1);
                    return;
                }
            }
        }

        System.out.println(Days - 1);
    }

    private static void Bfs() {
        while (!deque.isEmpty()) {
            int[] cur = deque.pollFirst();
            Left--;

            for (int i = 0; i < 4; i++ ){
                int ny = cur[0] + My[i];
                int nx = cur[1] + Mx[i];

                if (ny < 0 || ny >= N || nx < 0 || nx >=M || Used[ny][nx] == 1) continue;

                if (Graph[ny][nx] == 0) {
                    Graph[ny][nx] = 1;
                    Used[ny][nx] = 1;
                    deque.addLast(new int[]{ny, nx});
                }
            }

            if (Left == 0) {
                Days++;
                Left = deque.size();
            }
        }
    }
}