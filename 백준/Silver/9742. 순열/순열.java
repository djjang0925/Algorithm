import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder Sb = new StringBuilder();
    static char[] Arr, Path;
    static int[] Used;
    static int N, Cnt;
    static boolean Flag;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String line;

        while ((line = br.readLine()) != null) {
            st = new StringTokenizer(line);

            Arr = st.nextToken().toCharArray();
            N = Integer.parseInt(st.nextToken());
            Path = new char[Arr.length];
            Used = new int[Arr.length];
            Cnt = 0;
            Flag = false;

            Permutation(0);

            if (!Flag) {
                ToString();
            }
        }

        System.out.println(Sb.toString());
    }

    private static void Permutation(int lv) {
        if (lv == Arr.length) {
            Cnt++;

            if (Cnt == N) {
                Flag = true;
                ToString();
                return;
            }

            return;
        }

        for (int i = 0; i < Arr.length; i++) {
            if (Used[i] == 1) continue;

            Used[i] = 1;
            Path[lv] = Arr[i];

            Permutation(lv + 1);

            Used[i] = 0;
        }
    }

    private static void ToString() {
        for (char i : Arr) {
            Sb.append(i);
        }

        Sb.append(" ").append(N).append(" = ");

        if (Cnt == N) {
            for (char i : Path) {
                Sb.append(i);
            }
        } else {
            Sb.append("No permutation");
        }

        Sb.append('\n');
    }
}