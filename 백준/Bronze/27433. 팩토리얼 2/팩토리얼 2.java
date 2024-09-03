import java.util.*;

public class Main {
    static long Recursion(long num) {
        if (num == 1 || num == 0) return 1;

        return num *= Recursion(num - 1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long n = sc.nextLong();

        System.out.println(Recursion(n));
    }
}