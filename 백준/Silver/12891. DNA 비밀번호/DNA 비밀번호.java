import java.io.*;
import java.util.*;

public class Main {
    static int S, P;
    static char[] Str;
    static int[] Key = new int[4];
    static int[] CurrentCount = new int[4];
    static int Res = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        S = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());

        Str = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            Key[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < P; i++) {
            addChar(Str[i]);
        }

        if (isValid()) {
            Res++;
        }

        for (int i = P; i < S; i++) {
            addChar(Str[i]);
            removeChar(Str[i - P]);

            if (isValid()) {
                Res++;
            }
        }

        System.out.println(Res);
    }

    static void addChar(char c) {
        if (c == 'A') CurrentCount[0]++;
        else if (c == 'C') CurrentCount[1]++;
        else if (c == 'G') CurrentCount[2]++;
        else if (c == 'T') CurrentCount[3]++;
    }

    static void removeChar(char c) {
        if (c == 'A') CurrentCount[0]--;
        else if (c == 'C') CurrentCount[1]--;
        else if (c == 'G') CurrentCount[2]--;
        else if (c == 'T') CurrentCount[3]--;
    }

    static boolean isValid() {
        for (int i = 0; i < 4; i++) {
            if (CurrentCount[i] < Key[i]) {
                return false;
            }
        }
        return true;
    }
}