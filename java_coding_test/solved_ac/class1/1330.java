// 두 수 비교하기
// 숫자 비교는 == 사용
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();

        if (A > B) {
            System.out.println(">");
        } else if (A == B) {
            System.out.println("==");
        } else {
            System.out.println("<");
        }

		sc.close();
	}
}