import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] chess = {1, 1, 2, 2, 2, 8};
		
		for (int i = 0; i < chess.length; i++) {
			int n = Integer.parseInt(st.nextToken());
			
			sb.append((chess[i] - n) + " ");
		}
		
		System.out.println(sb.toString());
	}

}