import java.util.*;
import java.io.*;

public class Main {
	
	static int n, m;
	static int[][] field;
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	static Deque<int[]> root = new ArrayDeque<>();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		
		field = new int[n][m];
		
		for (int i = 0; i < field.length; i++) {
			st = new StringTokenizer(br.readLine());
		
			for (int j = 0; j < field[i].length; j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
				
				if (field[i][j] == 1) {
					root.add(new int[]{i, j});
				}
			}
		}
		
		bfs();
		
		int res = 0;
		for (int i = 0; i < field.length; i++) {
			for (int j = 0; j < field[i].length; j++) {
				if (field[i][j] == 0) {
					System.out.println(-1);
					return;
				}
				
				if (field[i][j] > res) {
					res = field[i][j];
				}
					
			}
		}
		
		System.out.println(res - 1);
		
	}
	
	static int bfs() {
		while (!root.isEmpty()) {
			int[] now = root.poll();
			int y = now[0];
			int x = now[1];
			
			for (int i = 0; i < 4; i++) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				
				if (ny >= n || ny < 0 || nx >= m || nx < 0) {
					continue;
				}
				
				if (field[ny][nx] == 0) {
					field[ny][nx] = field[y][x] + 1;
					root.add(new int[] {ny, nx});
				}
			}		
		}
		
		return 0;
	}
		
}