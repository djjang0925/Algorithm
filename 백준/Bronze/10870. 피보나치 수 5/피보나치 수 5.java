import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static List<Integer> Arr = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        Arr.add(0);
        Arr.add(1);

        Fibo();

        System.out.println(Arr.get(N));
    }

    private static void Fibo() {
        if (N < 2) return;

        int idx = Arr.size();

        Arr.add(Arr.get(idx - 2) + Arr.get(idx - 1));

        if (idx == N) {
            return;
        }

        Fibo();
    }
}