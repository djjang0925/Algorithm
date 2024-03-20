import java.io.*;
import java.util.*;

public class Main {
    static int w;
    static int h;
    static int count;
    static int[][] graph;
    static boolean[][] visited;
    static boolean exist;
    static int[] dx = {1, -1, 0, 0, 1, -1, 1, -1};
    static int[] dy = {0, 0, 1, -1, 1, -1, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        while (true) {
            exist = false;
            st = new StringTokenizer(br.readLine());

            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            graph = new int[h][w];
            visited = new boolean[h][w];
            count = 0;

            if (w == 0 && h == 0) {
                System.out.println(sb.toString());
                break;
            }

            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            findroot(graph);
            sb.append(count).append("\n");
        }
    }

    private static void findroot(int[][] graph) {
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    visited[i][j] = true;
                    count++;
                    bfs(i, j);
                }
            }
        }
    }

    private static void bfs(int y, int x) {
        Deque<int[]> root = new ArrayDeque<>();
        root.add(new int[]{y, x});

        while (!root.isEmpty()) {
            int[] now = root.pollLast();

            for (int i = 0; i < 8; i++) {
                int ny = now[0] + dy[i];
                int nx = now[1] + dx[i];

                if (ny < h && ny >= 0 && nx < w && nx >= 0) {
                    if (graph[ny][nx] == 1 && !visited[ny][nx]) {
                        visited[ny][nx] = true;
                        root.addFirst(new int[]{ny, nx});
                    }
                }
            }
        }
    }
}