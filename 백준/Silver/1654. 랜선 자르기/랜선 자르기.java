import java.util.*;
import java.io.*;

public class Main {
    static int K, N;
    static long[] Cables;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        Cables = new long[K];

        for (int i = 0; i < K; i++){
            Cables[i] = Long.parseLong(br.readLine());
        }

        long s = 1, l = Arrays.stream(Cables).max().getAsLong();

        while (s <= l) {
            long cnt = 0;
            long m = (s + l) / 2;

            for (long i : Cables) {
                cnt += i / m;
            }

            if (cnt < N) {
                l = m - 1;
            } else {
                s = m + 1;
            }
        }

        System.out.println(l);
    }
}