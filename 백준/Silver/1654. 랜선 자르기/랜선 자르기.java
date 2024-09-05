import java.util.*;
import java.io.*;

public class Main {
    static int K, N;
    static Long[] Cables;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        Cables = new Long[K];

        for (int i = 0; i < K; i++) {
            Cables[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(Cables);

        long max = Cables[K - 1];
        long min = 1;

        while(min <= max) {
            long cnt = 0;
            long mid = (max + min) / 2;

            for (long i : Cables) {
                cnt += i / mid;
            }

            if (cnt < N) {
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(min - 1);
    }
}