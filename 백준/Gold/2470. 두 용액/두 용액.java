import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] Arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        Arr = new int[N];

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < N; i++) {
            Arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(Arr);

        int s = 0, e = N - 1;
        int[] temp = {2000000001, 0, 0};

        while(s < e) {
            int sum = Arr[s] + Arr[e];

            if (Math.abs(sum) < temp[0]) {
                temp[0] = Math.abs(sum);
                temp[1] = Arr[s];
                temp[2] = Arr[e];
            }

            if (sum == 0) {
                break;
            } else if (sum < 0) {
                s++;
            } else {
                e--;
            }
        }

        sb.append(temp[1]).append(" ").append(temp[2]);
        System.out.println(sb.toString());
    }
}