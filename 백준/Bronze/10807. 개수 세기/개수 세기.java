import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int num = Integer.parseInt(br.readLine());
        int []arr = new int[num];
        int res = 0;

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < num; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int num2 = Integer.parseInt(br.readLine());

        for(int i = 0; i < num; i++) {
            if(arr[i] == num2) {
                res += 1;
            }
        }

        System.out.println(res);
    }
}