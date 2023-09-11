import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int a, b, c;
	static int flag;
	static int[] visited;
	static int[][] graph;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		graph = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < m; i++) {
			flag = 0;
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			visited = new int[n];
			visited[a - 1] = 1;
			take_time(a - 1, b - 1, c, 0);
			
			if (flag == 1) {
				sb.append("Enjoy other party" + '\n');
			}
			else {
				sb.append("Stay here" + '\n');
			}
		}
		
		System.out.println(sb.toString());
	}
	
	static int take_time(int a, int b, int c, int time) {
		if (flag == 1) {
			return 0;
		}
		
		if (a == b && time <= c) {
			flag = 1;
			return 0;
		}
		else if (time > c) {
			return 0;
		}
		
		for (int i = 0; i < n; i++) {
			if (a == i) {
				continue;
			}
			
			if (visited[i] == 0) {
				visited[i] = 1;
				take_time(i, b, c, time + graph[a][i]);
				visited[i] = 0;
			}
		}
		
		return 0;
	}

}