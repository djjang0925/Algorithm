import java.util.*;
import java.io.*;

public class Main {
    static char[][] Graph = new char[5][5];
    static int[] Dy = {1, -1, 0, 0};
    static int[] Dx = {0, 0, 1, -1};
    static int Result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 5; i++) {
            Graph[i] = br.readLine().toCharArray();
        }

        FindCombination(new ArrayList<>(), 0, 0);

        System.out.println(Result);
    }

    private static void FindCombination(List<Integer> selected, int start, int sCount) {
        if (selected.size() == 7) {
            if (sCount >= 4 && IsClosed(selected)) {
                Result++;
            }
            return;
        }

        for (int i = start; i < 25; i++) {
            int y = i / 5;
            int x = i % 5;

            selected.add(i);
            FindCombination(selected, i + 1, sCount + (Graph[y][x] == 'S' ? 1 : 0));
            selected.remove(selected.size() - 1);
        }
    }

    private static boolean IsClosed(List<Integer> selected) {
        Deque<Integer> deque = new ArrayDeque<>();
        boolean[] visited = new boolean[25];
        deque.addLast(selected.get(0));
        visited[selected.get(0)] = true;
        int count = 1;

        while (!deque.isEmpty()) {
            int current = deque.pollFirst();
            int y = current / 5;
            int x = current % 5;

            for (int i = 0; i < 4; i++) {
                int ny = y + Dy[i];
                int nx = x + Dx[i];
                int next = ny * 5 + nx;

                if (ny < 0 || nx < 0 || ny >= 5 || nx >= 5) {
                    continue;
                }

                if (selected.contains(next) && !visited[next]) {
                    visited[next] = true;
                    deque.addLast(next);
                    count++;
                }
            }
        }

        return count == 7;
    }
}