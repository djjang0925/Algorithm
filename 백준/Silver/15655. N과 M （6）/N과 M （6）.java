import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] Arr, Path;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        Arr = new int[N];
        Path = new int[M];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            Arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(Arr);

        Combination(0, 0);

        System.out.println(sb.toString());
    }

    static void Combination(int lv, int st) {
        if (lv == M) {
            ToString();
            return;
        }

        for (int i = st; i < N; i++) {
            Path[lv] = Arr[i];
            Combination(lv + 1, i + 1);
        }
    }

    static void ToString() {
        for (int i : Path) {
            sb.append(i).append(" ");
        }

        sb.append('\n');
    }
}