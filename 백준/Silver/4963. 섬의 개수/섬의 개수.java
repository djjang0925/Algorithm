import java.util.*;
import java.io.*;

public class Main {
    static int W, H;
    static int[][] Graph, Visited;
    static int Island;
    static Deque<int[]> Dq = new ArrayDeque<>();
    static int[] My = {1, -1, 0, 0, 1, -1, 1, -1};
    static int[] Mx = {0, 0, 1, -1, -1, 1, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (true) {
            Island = 0;

            st = new StringTokenizer(br.readLine());

            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());

            if (W == 0 && H == 0) break;

            Graph = new int[H][W];
            Visited = new int[H][W];

            for (int i = 0; i < H; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < W; j++) {
                    Graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    if (Graph[i][j] == 1) {
                        Bfs(i, j);
                    }
                }
            }
            sb.append(Island).append('\n');
        }

        System.out.println(sb.toString());
    }

    private static void Bfs(int y, int x) {
        Dq.addLast(new int[]{y, x});
        Visited[y][x] = 1;
        Graph[y][x] = 0;

        while (!Dq.isEmpty()) {
            int[] cur = Dq.pollFirst();
            int cy = cur[0], cx = cur[1];

            for (int i = 0; i < 8; i++) {
                int ny = cy + My[i];
                int nx = cx + Mx[i];

                if (ny < 0 || ny >= H || nx < 0 || nx >= W || Visited[ny][nx] == 1) {
                    continue;
                }

                if (Graph[ny][nx] == 1) {
                    Visited[ny][nx] = 1;
                    Graph[ny][nx] = 0;
                    Dq.addLast(new int[]{ny, nx});
                }
            }
        }

        Island++;
    }
}