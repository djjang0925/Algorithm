import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] Path, Used;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        Path = new int[N];
        Used = new int[N];

        Permutation(0);

        System.out.println(sb.toString());
    }

    static void Permutation(int lv) {
        if (lv == N) {
            ToString();
            return;
        }

        for (int i = 0; i < N; i++) {
            if (Used[i] == 1) continue;

            Used[i] = 1;
            Path[lv] = i + 1;
            Permutation(lv + 1);
            Used[i] = 0;
        }
    }

    static void ToString() {
        for (int i : Path) {
            sb.append(i).append(" ");
        }

        sb.append('\n');
    }
}