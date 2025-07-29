// ACM 호텔
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; ++t) {
            int H = sc.nextInt();
            int W = sc.nextInt();
            int N = sc.nextInt();

            int q = N % H;
            int r = N / H + 1;

            if (q == 0) {
                q = H;
                r = N / H;
            }

            System.out.println(q * 100 + r);
        }

		sc.close();
	}
}