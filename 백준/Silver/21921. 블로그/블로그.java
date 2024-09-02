import java.io.*;
import java.util.*;

public class Main {
    static int N, X, Max = 0, Cnt = 0;
    static int[] Nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Nums = new int[N];

        for (int i = 0; i < N; i++) {
            Nums[i] = Integer.parseInt(st.nextToken());
        }

        int s = 0, e = X - 1, temp = 0;

        for (int i = 0; i < X; i++) {
            temp += Nums[i];
        }

        while (e < N) {
            if (temp == Max && temp > 0) {
                Cnt++;
            } else if (temp > Max) {
                Max = temp;
                Cnt = 1;
            }

            if (e == N - 1) {
                break;
            } else {
                temp = temp - Nums[s++] + Nums[++e];
            }
        }

        if (Max == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(Max);
            System.out.println(Cnt);
        }
    }
}