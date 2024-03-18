import java.io.*;
import java.util.*;

public class Main {
    static Boolean[][] graph;
    static Boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        graph = new Boolean[n + 1][n + 1];
        visited = new Boolean[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = true;
            graph[b][a] = true;
        }

        dfs();
    }

    private static void dfs() {
        int count = 0;

        Stack<Integer> stack = new Stack<Integer>();
        stack.push(1);

        while (!stack.isEmpty()) {
            int now = stack.pop();
            visited[now] = true;
            count++;

            for (int i = 1; i < graph[now].length; i++) {
                if (graph[now][i] != null && graph[now][i] && visited[i] == null) {
                    visited[i] = true;
                    stack.push(i);
                }
            }
        }

        System.out.println(count - 1);
    }
}