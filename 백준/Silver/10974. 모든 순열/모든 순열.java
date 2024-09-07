import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder Sb = new StringBuilder();
    static int N;
    static int[] Used, Path;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        Used = new int[N];
        Path = new int[N];

        Permutation(0);

        System.out.println(Sb.toString());
    }

    private static void Permutation(int n) {
        if (n == N) {
            Print();
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (Used[i - 1] == 0) {
                Used[i - 1] = 1;
                Path[n] = i;

                Permutation(n + 1);

                Used[i - 1] = 0;
            }
        }
    }

    private static void Print() {
        for (int i : Path) {
            Sb.append(i).append(" ");
        }

        Sb.append('\n');
    }
}