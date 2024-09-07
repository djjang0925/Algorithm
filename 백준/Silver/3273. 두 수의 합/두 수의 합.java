import java.util.*;
import java.io.*;

public class Main {
    static int N, X;
    static int[] Numbers;
    static int Cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        Numbers = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            Numbers[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(Numbers);

        X = Integer.parseInt(br.readLine());

        int s = 0, e = N - 1;

        while(s < e) {
            int sum = Numbers[s] + Numbers[e];

            if (sum == X) {
                s++;
                e--;
                Cnt++;
            } else if (sum > X) {
                e--;
            } else {
                s++;
            }
        }

        System.out.println(Cnt);
    }
}