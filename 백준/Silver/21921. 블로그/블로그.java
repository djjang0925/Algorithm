import java.util.*;
import java.io.*;

public class Main {
    static int N, X;
    static int[] Visited;
    static int Cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        Visited = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            Visited[i] = Integer.parseInt(st.nextToken());
        }

        int max = -1;
        int cur = 0;

        for (int i = 0; i < X; i++) {
            cur += Visited[i];
        }

        int s = 0, e = X - 1;

        while(true) {
            if (cur > max) {
                max = cur;
                Cnt = 1;
            } else if (cur == max) {
                Cnt++;
            }

            if (e == N - 1) break;

            cur = cur - Visited[s++] + Visited[++e];
        }

        if (max == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(max);
            System.out.println(Cnt);
        }
    }
}