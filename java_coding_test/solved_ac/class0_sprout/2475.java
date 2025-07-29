// 검증수
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        long totalSum = 0;
        long num = 0;
        for (int i = 0; i < 5; ++i) {
            num = sc.nextLong();
            totalSum += num * num;
        }

        System.out.println(totalSum % 10);

		sc.close();
	}
}