import java.util.*;
import java.io.*;

public class Main {
    static class Point {
        int z, y, x;

        Point(int z, int y, int x) {
            this.z = z;
            this.y = y;
            this.x = x;
        }
    }
    static int M, N, H;
    static int[][][] Graph;
    static Deque<Point> Root = new ArrayDeque<>();
    static int[] Dh = {1, -1, 0, 0, 0, 0};
    static int[] Dy = {0, 0, 1, -1, 0, 0};
    static int[] Dx = {0, 0, 0, 0, 1, -1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        Graph = new int[H][N][M];

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());

                for (int k = 0; k < M; k++) {
                    int n = Integer.parseInt(st.nextToken());

                    if (n == 1) {
                        Root.addLast(new Point(i, j, k));
                    }

                    Graph[i][j][k] = n;
                }
            }
        }

        Bfs();
    }

    private static void Bfs() {
        while(!Root.isEmpty()) {
            Point current = Root.pollFirst();

            int h = current.z;
            int y = current.y;
            int x = current.x;

            for (int i = 0; i < 6; i++) {
                int nh = h + Dh[i];
                int ny = y + Dy[i];
                int nx = x + Dx[i];

                if (nh >= H || ny >= N || nx >= M || nh < 0 || ny < 0 || nx < 0) {
                    continue;
                }

                if (Graph[nh][ny][nx] == 0) {
                    Graph[nh][ny][nx] = Graph[h][y][x] + 1;

                    Root.addLast(new Point(nh, ny, nx));
                }
            }
        }

        int max = 0;

        for (int[][] i : Graph) {
            for (int[] j : i) {
                for(int k : j) {
                    if (max < k) {
                        max = k;
                    }

                    if (k == 0) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }

        System.out.println(max - 1);
    }
}