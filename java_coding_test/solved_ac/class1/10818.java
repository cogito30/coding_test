// 최소, 최대
import java.util.Scanner;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; ++i) {
            arr[i]  = sc.nextInt();
        }

        // int minNum = arr[0];
        // int maxNum = arr[0];
        // for (int i = 0; i < N; ++i) {
        //     if (arr[i] < minNum) {
        //         minNum = arr[i];
        //     }
        //     if (arr[i] > maxNum) {
        //         maxNum = arr[i];
        //     }
        // }
        // System.out.println(minNum + " " + maxNum);

        Arrays.sort(arr);
        System.out.println(arr[0] + " " + arr[N - 1]);

		sc.close();
	}
}