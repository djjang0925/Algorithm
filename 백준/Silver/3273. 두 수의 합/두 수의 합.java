import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        int res = 0;

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int x = Integer.parseInt(br.readLine());

        Arrays.sort(numbers);

        int start = 0;
        int end = n - 1;

        while (start < end) {
            if (numbers[start] + numbers[end] == x) {
                res++;
                start++;
                end--;
            } else if (numbers[start] + numbers[end] < x) {
                start++;
            } else {
                end--;
            }
        }

        System.out.println(res);
    }
}