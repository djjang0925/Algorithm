import java.util.*;
import java.io.*;

public class Main {
    static List<Integer> list;
    static int[] Path;
    static StringBuilder Sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        while(true) {
            list = new ArrayList<>();
            st = new StringTokenizer(br.readLine());

            Path = new int[6];

            if (Integer.parseInt(st.nextToken()) == 0) {
                break;
            }

            while(st.hasMoreTokens()) {
                list.add(Integer.parseInt(st.nextToken()));
            }

            list.sort(Comparator.naturalOrder());
            Combination(0,0 );
            Sb.append('\n');
        }

        bw.write(Sb.toString());
        bw.flush();
        bw.close();
    }

    static void Combination(int lv, int st) {
        if (lv == 6) {
            Print(Path);
            return;
        }

        for (int i = st; i < list.size(); i++) {
            Path[lv] = list.get(i);
            Combination(lv + 1, i + 1);
        }
    }

    static void Print(int[] arr) {
        for (int i : arr) {
            Sb.append(i).append(" ");
        }

        Sb.append('\n');
    }
}