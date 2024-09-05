import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static HashMap<Integer, Integer> Set = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N + 1; i++) {
            Set.put(i, i);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int command = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (command == 0) {
                Union(a, b);
            } else {
                if (Find(a) == Find(b)) {
                    sb.append("YES\n");
                } else {
                    sb.append("NO\n");
                }
            }
        }

        System.out.println(sb.toString());
    }

    private static int Find(int a) {
        if (Set.get(a) == a) {
            return a;
        }

        int parent = Find(Set.get(a));
        Set.put(a, parent);

        return parent;
    }

    private static void Union(int a, int b) {
        int fa = Find(a);
        int fb = Find(b);

        if (fa == fb) return;
        
        Set.put(fb, fa);
    }
}