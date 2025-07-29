// 팩토리얼
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();

        long answer = 1;
        for (int i = 1; i <= N; ++i) {
            answer *= i;
        }

        System.out.println(answer);
		sc.close();
	}
}