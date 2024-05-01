import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
// Arrays.sort(A);
/*
    문제:
    갑옷 재료는 고유 번호 존재, 갑온은 2개의 재료로 만들음
    두 재료 고유번호 합쳐서 M이 되면 갑옷 만들어짐
    N개의 재료로 갑옷 몇 개 만들 수 있는지 출력

    조건:
    1<=M<=10,000,000 천만
    1<=N<=15,000
    고유번호 <=100,000 십만

    입력:
    N
    M
    재료 고유번호1 고유번호2 ... -> N개

    풀이:
    O(nlogn)도 괜찮음
    정렬 후 투포인터 사용
    1. A[S]+A[E] > M : E--;
    2. A[S]+A[E] < M : S++;
    3. A[S]+A[E] == M : S++; E--; cnt++;
 */
public class 백준1940_주몽의_명령_투포인터 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine());
        int M = Integer.parseInt(bufferedReader.readLine());
        int[] A = new int[N];

        StringTokenizer st = new StringTokenizer(bufferedReader.readLine());
        for(int i=0; i<N; i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        int cnt = 0;
        int s = 0;
        int e = N-1;

        while (s<e){
            if(A[s]+A[e] < M) s++;
            else if (A[s]+A[e] > M) e--;
            else {
                cnt++;
                s++;
                e--;
            }
        }
        System.out.println(cnt);
    }
}
