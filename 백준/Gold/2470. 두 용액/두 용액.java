import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] Nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        Nums = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            Nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(Nums);

        int s = 0, e = N - 1, sum = 2000000000;
        int r1 = 0, r2 = 0;

        while (s < e) {
            int temp = Nums[s] + Nums[e];

            if (Math.abs(temp) < sum) {
                sum = Math.abs(temp);
                r1 = Nums[s];
                r2 = Nums[e];
            }

            if (temp == 0) {
                break;
            } else if (temp < 0) {
                s++;
            } else {
                e--;
            }
        }

        sb.append(r1).append(" ").append(r2);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}