import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
    숫자 N개가 주어졌을 때 i번째 수부터 j번째 수까지의 합 구하기
    1<=N<=10만, 1<=M(합을 구해야 하는 횟수)<=10만
 */
public class 백준11659_구간_합_구하기_합배열 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader =
                new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer =
                new StringTokenizer(bufferedReader.readLine());

        // 첫 번째 줄 데이터 받음
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());

        long[] S = new long[N+1];
        // 덧셈 곱셈이 많으면 int 범위를 넘어갈 수 있어서 습관적으로 숫자를 다룰 땐 long형 사용하면 좋음

        // 두 번째 줄에 데이터 받으며 동시에 합배열 생성
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i=1; i<=N; i++){
            S[i] = S[i-1] + Integer.parseInt(stringTokenizer.nextToken());
        }

        // 범위 입력받고 합 출력
        for (int j=0; j<M; j++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());

            System.out.println(S[end] - S[start-1]);
        }

    }
}
/*
1 <= N, M <= 100,000 : 10만
받는 데이터가 많을 때는 scanner 보다 bufferedReader가 시간측면에서 유리
한 줄에 많은 데이터를 받아야 하는 경우 : StringTokenizer
 */