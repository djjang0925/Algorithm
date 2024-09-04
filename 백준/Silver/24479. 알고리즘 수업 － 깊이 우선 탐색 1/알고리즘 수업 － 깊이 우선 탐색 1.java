import java.util.*;
import java.io.*;

public class Main {
    static int N, M, R;
    static HashMap<Integer, List<Integer>> Graph = new HashMap<>();
    static int[] Used;
    static int Cnt = 1;
    static int[] Path;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        Used = new int[N + 1];
        Path = new int[N];

        for (int i = 0; i < N; i++) {
            Graph.put(i + 1, new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Graph.get(a).add(b);
            Graph.get(b).add(a);
        }

        for (int i = 1; i < N + 1; i++) {
            Graph.get(i).sort(Comparator.naturalOrder());
        }

        dfs(R);

        for (int i : Path) {
            System.out.println(i);
        }
    }

    private static void dfs(int r) {
        Path[r - 1] = Cnt++;
        Used[r] = 1;

        for (int i : Graph.get(r)) {
            if (Used[i] != 1) dfs(i);
        }
    }

}