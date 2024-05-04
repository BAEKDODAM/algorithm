import java.util.Scanner;
/*
    M이상 N이하의 소수 구하기
    1<=M<=N<=1,000,000

    일반적인 소수 구하기 방법으로 풀면 시간초과 발생함
    -> 에라토스테네스 채 방법으로 풀어야 함
    1. N+1 크기의 배열 선언 후 각 인덱스 값으로 채움
    2. 1은 소수 아니므로 삭제(0으로 변경)
    3. 2부터 N의 제곱근(루트N)까지의 값을 탐색
    4. 값이 인덱스 값으면 그대로 두고 그 값의 배수를 탐색해 0으로 변경
    5. 배열에 남은 수 중 N 이상 M 이하의 수 모두 출력
 */
public class 백준1929_소수구하기_에라토스테네스의채 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        int[] A = new int[N+1];
        for (int i=2; i<=N; i++){
            A[i] = i;
        }
        for (int i=2; i<=Math.sqrt(N); i++){
            if (A[i]==0)continue;
            for(int j=i+i; j<=N; j=j+i){
                A[j] = 0; // 소수의 배수이면 소수 아님
            }
        }
        for(int i=M; i<=N; i++){
            if(A[i] != 0) System.out.println(A[i]);
        }

    }
}
