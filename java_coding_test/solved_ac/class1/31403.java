// A + B - C
// Integer는 toString이 가능하지만 int는 불가능
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        System.out.println(A + B - C);

        int answer = Integer.parseInt(String.valueOf(A) + String.valueOf(B)) - C;
        System.out.println(answer);

		sc.close();
	}
}