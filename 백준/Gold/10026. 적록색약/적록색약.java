import java.io.*;
import java.util.*;

public class Main {
	
	static char[][] graph;
	static boolean[][] visited;
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	static int n;
	static Deque<int[]> root = new ArrayDeque<>();	
	
	static int bfs() {
		while(!root.isEmpty()) {
			int[] now = root.poll();
			int y = now[0];
			int x = now[1];
			
			for (int i = 0; i < 4; i++) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				
				if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
					continue;
				}
				
				if (visited[ny][nx] == false && graph[ny][nx] == graph[y][x]) {
					visited[ny][nx] = true;
					root.add(new int[] {ny, nx});
				}
				
			}
			
		}
		
		return 0;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		n = Integer.parseInt(br.readLine());
		graph = new char[n][n];
		int res = 0;
		
		for (int i = 0; i < n; i++) {
			String temp = br.readLine();
			
			graph[i] = temp.toCharArray();
		}
		
		for (int k = 0; k < 2; k++) {
			visited = new boolean[n][n];
			
			if (k == 1) {
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						if (graph[i][j] == 'R') {
							graph[i][j] = 'G';
						}
					}
				}
			}
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (visited[i][j] == false) { 
						res ++;
						visited[i][j] = true;
						root.add(new int[] {i, j});
						bfs();
					}
				}
			}
			sb.append(res + " ");
			res = 0;
		}
		
		System.out.println(sb.toString());
	}

}