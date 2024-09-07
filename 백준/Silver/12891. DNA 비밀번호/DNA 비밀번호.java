import java.util.*;
import java.io.*;

public class Main {
    static int S, P;
    static char[] Arr;
    static int[] Key, Used;
    static int Cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        S = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        Key = new int[4];
        Used = new int[4];

        Arr = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 4; i++) {
            Key[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < P; i++) {
            AddChar(Arr[i]);
        }

        int s = 0, e = P - 1;

        while (true) {
            IsValid();

            if (e == S - 1) break;

            AddChar(Arr[++e]);
            RemoveChar(Arr[s++]);
        }

        System.out.println(Cnt);
    }

    private static void RemoveChar(char c) {
        if (c == 'A') {
            Used[0] -= 1;
        } else if (c == 'C') {
            Used[1] -= 1;
        } else if (c == 'G') {
            Used[2] -= 1;
        } else if (c == 'T') {
            Used[3] -= 1;
        }
    }

    private static void IsValid() {
        for (int i = 0; i < 4; i++) {
            if (Used[i] < Key[i]) {
                return;
            }
        }

        Cnt++;
    }

    private static void AddChar(char c) {
        if (c == 'A') {
            Used[0] += 1;
        } else if (c == 'C') {
            Used[1] += 1;
        } else if (c == 'G') {
            Used[2] += 1;
        } else if (c == 'T') {
            Used[3] += 1;
        }
    }
}