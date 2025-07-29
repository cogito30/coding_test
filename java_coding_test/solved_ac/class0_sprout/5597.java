// 과제 안 내신 분..?
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[30];

        for (int i = 0; i < 30; ++i) {
            arr[i] = 0;
        }

        int num = 0;
        for (int i = 0; i < 28; ++i) {
            num = sc.nextInt();
            arr[num - 1]++;
        }

        for (int i = 0; i < 30; ++i) {
            if (arr[i] == 0) {
                System.out.println(i + 1);
            }
        }
    }
}
