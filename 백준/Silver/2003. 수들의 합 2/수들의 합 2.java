import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] Nums;
    static int Res = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        Nums = new int[N];

        for (int i = 0; i < N; i++) {
            Nums[i] = Integer.parseInt(st.nextToken());
        }

        int s = 0, e = 0, temp = Nums[0];

        while(true) {
            if (temp == M) {
                Res++;

                temp -= Nums[s++];
            } else if (temp < M) {
                if (e == N - 1) {
                    break;
                }

                temp += Nums[++e];
            } else {
                temp -= Nums[s++];
            }
        }

        System.out.println(Res);
    }
}