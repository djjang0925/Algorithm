import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] Budgets;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        Budgets = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            Budgets[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        Arrays.sort(Budgets);

        int max = Budgets[N - 1];
        int min = 1;

        while (min <= max) {
            int total = 0;
            int mid = (max + min) / 2;

            for (int i : Budgets) {
                if (i > mid) {
                    total += mid;
                } else {
                    total += i;
                }
            }

            if (total > M) {
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(max);
    }
}