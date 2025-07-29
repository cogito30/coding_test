// 숫자의 합
// 문자열 입력 주의 nextLine 대신 next 사용
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String s = sc.next();

        int totalSum = 0;
        for (int i = 0; i < N; ++i) {
            totalSum += s.charAt(i) - '0';
        }

        System.out.println(totalSum);

		sc.close();
	}
}