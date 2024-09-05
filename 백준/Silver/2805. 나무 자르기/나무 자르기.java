import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static long[] Trees;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        Trees = new long[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            Trees[i] = Long.parseLong(st.nextToken());
        }

        long s = 0;
        long l = Arrays.stream(Trees).max().getAsLong();

        while (s < l) {
            long total = 0;
            long m = (s + l) / 2;

            for (long i : Trees) {
                if (i >= m) {
                    total += i - m;
                }
            }

            if (total < M) {
                l = m;
            } else {
                s = m + 1;
            }
        }

        System.out.println(l - 1);
    }
}