// 학점계산
import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        String s = sc.next();
        double grade = 0.0;
        char ch = s.charAt(0);
        if (ch == 'A') {
            grade = 4.0;
        } else if (ch == 'B') {
            grade = 3.0;
        } else if (ch == 'C') {
            grade = 2.0;
        } else if (ch == 'D') {
            grade = 1.0;
        } else {
            grade = 0.0;
        }

        ch = s.charAt(1);
        if (ch == '+') {
            grade += 0.3;
        } else if (ch == '-') {
            grade -= 0.3;
        }

        System.out.println(grade);

		sc.close();
	}
}