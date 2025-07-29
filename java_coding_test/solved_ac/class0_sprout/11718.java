// 그대로 출력하기
// Scanner 메서드: nextLine(), hasNextLine()
import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        while (sc.hasNextLine()) {
            String s = sc.nextLine();
            System.out.println(s);
        }

		sc.close();
	}
}