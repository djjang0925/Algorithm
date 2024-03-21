import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] graph;
    static Deque<Deque<int[]>> root = new ArrayDeque<>();
    static int size;
    static int[] dy = {1, -1, 0, 0};
    static int[] dx = {0, 0, 1, -1};
    static int res = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        size = m * n;
        graph = new int[n][m];

        Deque<int[]> tomatos = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == 1) {
                    tomatos.addFirst(new int[]{i, j});
                    size--;
                } else if (graph[i][j] == -1) {
                    size--;
                }
            }
        }

        root.addFirst(tomatos);

        bfs();
    }

    private static void bfs() {
        while (!root.isEmpty()) {
            res++;
            Deque<int[]> today = root.pollFirst();
            Deque<int[]> tomorrow = new ArrayDeque<>();

            while (!today.isEmpty()) {
                int[] now = today.pollLast();

                for (int i = 0; i < 4; i++) {
                    int ny = now[0] + dy[i];
                    int nx = now[1] + dx[i];

                    if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
                        if (graph[ny][nx] == 0) {
                            graph[ny][nx] = 1;
                            size--;
                            tomorrow.addFirst(new int[]{ny, nx});
                        }
                    }
                }
            }

            if (!tomorrow.isEmpty()) {
                root.addFirst(tomorrow);
            }
        }

        if (size == 0) {
            System.out.println(res);
        } else {
            System.out.println(-1);
        }
    }
}