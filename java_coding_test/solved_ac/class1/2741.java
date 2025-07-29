// N 찍기
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();

        for (int i = 0; i < N; ++i) {
            System.out.println(i + 1);
        }

		sc.close();
	}
}