import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static List<Integer> Fibo = new ArrayList<>(Arrays.asList(0, 1));
    static void Recursion() {
        int idx = Fibo.size();
        if (N < 2) return;

        if (idx == N) Fibo.add(Fibo.get(idx - 1) + Fibo.get(idx - 2));
        else if (idx < N) {
            Fibo.add(Fibo.get(idx - 1) + Fibo.get(idx - 2));
            Recursion();
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        Recursion();
        System.out.println(Fibo.get(N));
    }
}