import java.util.*;
import java.io.*;

public class Main {
    static int K;
    static int[] Arr;
    static int[] Path;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        while(true) {
            Path = new int[6];
            st = new StringTokenizer(br.readLine());
            K = Integer.parseInt(st.nextToken());

            if (K == 0) break;

            Arr = new int[K];
            for (int i = 0; i < K; i++) {
                Arr[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(Arr);

            Combination(0, 0);
            sb.append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void Combination(int lv, int st) {
        if (lv == 6) {
            Print();
            return;
        }

        for (int i = st; i < K; i++) {
            Path[lv] = Arr[i];
            Combination(lv + 1, i + 1);
        }
    }

    static void Print() {
        for (int i : Path) {
            sb.append(i).append(" ");
        }

        sb.append('\n');
    }
}