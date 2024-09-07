import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(br.readLine());

        System.out.println(Recursion(N));
    }

    private static long Recursion(long n) {
        if (n == 0) {
            return 1;
        }

        return n * Recursion(n - 1);
    }
}