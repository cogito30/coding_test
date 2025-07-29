// 빠른 A + B
// BufferedReader, BufferedWriter 사용
// BufferReader 사용시 IOException 예외처리가 필수
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(bf.readLine());
        for (int t = 0; t < T; ++t) {
            String s = bf.readLine();
            int A = Integer.parseInt(s.split(" ")[0]);
            int B = Integer.parseInt(s.split(" ")[1]);
            bw.write(A + B + "\n");  // 버퍼에 작성
        }
        bw.flush();  // 화면에 출력
	}
}