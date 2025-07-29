// X보다 작은수
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int X = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; ++i) {
            arr[i] = sc.nextInt();
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; ++i) {
            if (arr[i] < X) {
                sb.append(arr[i] + " ");
            }
        }
        System.out.println(sb.toString().trim());
	}
}
