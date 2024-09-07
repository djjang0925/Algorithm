import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static HashMap<Integer, Integer> Cities = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            Cities.put(i, 0);
        }

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 1; j <= N; j++) {
                if (Integer.parseInt(st.nextToken()) == 1) {
                    Union(i, j);
                }
            }
        }

        st = new StringTokenizer(br.readLine());

        int d = Find(Integer.parseInt(st.nextToken()));

        for (int i = 1; i < M; i++) {
            if (d != Find(Integer.parseInt(st.nextToken()))) {
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }

    private static void Union(int i, int j) {
        int fi = Find(i);
        int fj = Find(j);

        if (fi == fj) return;

        Cities.put(fj, fi);
    }

    private static int Find(int i) {
        if (Cities.get(i) == 0) return i;

        int parent = Find(Cities.get(i));
        Cities.put(i, parent);

        return parent;
    }
}