// 문자열
// 문자열 처리 주의!!
import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine()); // 정수 입력 후 줄바꿈까지 처리

        for (int t = 0; t < T; ++t) {
            String s = sc.nextLine();
            char ch1 = s.charAt(0);
            char ch2 = s.charAt(s.length() - 1);
            System.out.println(ch1 + "" + ch2);
        }

		sc.close();
	}
}