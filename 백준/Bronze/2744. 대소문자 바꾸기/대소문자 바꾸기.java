import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		char[] arr = str.toCharArray();
		
		for (int i = 0; i < arr.length; i++) {
			if (Character.isLowerCase(arr[i])) {
				System.out.print(Character.toUpperCase(arr[i]));
			}
			else if (Character.isUpperCase(arr[i])) {
				System.out.print(Character.toLowerCase(arr[i]));
			}
		}
	}
}