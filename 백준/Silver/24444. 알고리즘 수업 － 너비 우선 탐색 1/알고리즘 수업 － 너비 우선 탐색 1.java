import java.util.*;
import java.io.*;

public class Main {
    static int N, M, R;
    static List<Integer>[] Graph;
    static int[] Visited, Order;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        Graph = new ArrayList[N + 1];
        Visited = new int[N];
        Order = new int[N];

        for (int i = 0; i <= N; i++) {
            Graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            Graph[x].add(y);
            Graph[y].add(x);
        }

        for (int i = 0; i < N + 1; i++) {
            Collections.sort(Graph[i]);
        }

        Bfs(R);

        for (int i : Order) {
            System.out.println(i);
        }
    }

    private static void Bfs(int r) {
        int cnt = 1;
        Deque<Integer> deque = new ArrayDeque<>();
        deque.addLast(r);

        while (!deque.isEmpty()) {
            int cur = deque.pollFirst();

            if (Visited[cur - 1] == 0) {
                Visited[cur - 1] = 1;
                Order[cur - 1] = cnt++;

                for (int i : Graph[cur]) {
                    deque.addLast(i);
                }
            }
        }
    }


}