import java.util.Scanner;
/*
    문제)
    2*N 크기의 직사각형을 2*1, 1*2 크기의 타일로 채우는 방법의 수 리턴
    1<=N<=1,000

    풀이) DP 사용
    N을 만드는 경우의 수
    = N-1을 만드는 경우의 수에서 맨 뒤에 세로 타일만 추가하는 경우
      + N-2를 만드는 경우의 수에서 가로 타일 두개 추가하는 경우
    이 과정이 반복되기 때문에 **DP**
 */
public class 백준11726_2N타일채우기_DP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long D[] = new long[1001];
        D[1]=1;
        D[2]=2;
        for(int i=3; i<=N; i++){
            D[i] = (D[i-1]+D[i-2]) %10007;
        }
        System.out.println(D[N]);
    }
}
