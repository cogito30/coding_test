// 행렬 덧셈
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] matrixA = new int[N][M];
        int[][] matrixB = new int[N][M];

        int num = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                num = sc.nextInt();
                matrixA[i][j] = num;
            }
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                num = sc.nextInt();
                matrixB[i][j] = num;
            }
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                matrixA[i][j] += matrixB[i][j];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                sb.append(matrixA[i][j] + " ");
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}
