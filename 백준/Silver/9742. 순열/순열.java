import java.util.*;
import java.io.*;

public class Main {
    static char[] Arr, Path;
    static int[] Used;
    static String Str;
    static int N, Cnt;
    static boolean Flag;
    static StringBuilder Sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String line;

        while ((line = br.readLine()) != null) {
            Flag = false;
            Cnt = 0;
            st = new StringTokenizer(line);
            Str = st.nextToken();
            N = Integer.parseInt(st.nextToken());
            Arr = Str.toCharArray();
            Path = new char[Arr.length];
            Used = new int[Arr.length];

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

        if (Flag) {
            for (char i : Path) {
                Sb.append(i);
            }
        } else {
            Sb.append("No permutation");
        }

        Sb.append('\n');
    }
}