// 단어의 개수
// 문자열이 공백으로 시작 및 끝낼수 있음 주의!!
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        s = s.trim();
        String[] strArray = s.split(" ");

        if (s.equals("")) {
            System.out.println(0);
        } else {
            System.out.println(strArray.length);
        }

		sc.close();
	}
}