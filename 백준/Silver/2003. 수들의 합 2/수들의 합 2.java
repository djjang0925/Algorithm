import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] numbers = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int res = 0;

        for (int i = 0; i < n; i++) {
            if (numbers[i] == m) {
                res++;
            } else if (numbers[i] < m) {
                int temp = numbers[i];
                int j = 1;

                while(temp <= m && i + j < n) {
                    temp += numbers[i + j];

                    if (temp == m) {
                        res++;
                        break;
                    } else if (temp < m) {
                        j++;
                    } else {
                        break;
                    }
                }
            }
        }

        System.out.println(res);
    }
}