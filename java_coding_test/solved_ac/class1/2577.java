// 숫자의 개수
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        long total = A * B * C;

        int[] arr = new int[10];
        int num = 0;
        while (total > 0) {
            num = total % 10;
            arr[num]++;
            total /= 10;
        }

        for (int i = 0; i < 10; ++i) {
            System.out.println(arr[i]);
        }

		sc.close();
	}
}