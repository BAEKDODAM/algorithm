import java.util.Arrays;
import java.util.Scanner;
/*
    - Arrays.sort(배열) = O(nlogn) ~ O(n^2)
    - 이진탐색 O(logn) 데이터가 천만 넘어가면 사용
        - 조건: 배열이 정렬되어 있어야함
        - 탐색 범위를 절반씩 줄여나감 -> 시작점, 중간점(시작+끝)/2, 끝점
        - 중간점과 찾을 값 비교 (while 시작점 <= 종료점
          if 같으면: 끝
          if 중간점 > 찾을 값: 중간점+1이 시작점이 되고 새로운 중간점을 구한 뒤 다시 찾기 반복
          if 중간점 < 찾을 값: 중간점-1이 끝점이 되고 새로운 중간점을 구한 뒤 다시 찾기 반복
 */

/*
    Q. N개의 정수에 특정 정수가 존재하는지 M번 확인
    1<=N,M<=100,000
    정수 범위 -231~231

    입력: 데이터 개수 N, 데이터 set, 찾아야 할 정수 개수 M, 정수 set

    풀이. O(nlogn) 이어야함
    이진탐색 사용
    1. 정수 배열 A 정렬 (Arrays.sort()사용) -> nlonn
    2. 특정 정수 x가 존재하는지 이진탐색
        1. A에서 중앙 값 찾기
        2. 중앙값과 x 비교
           중앙값 < x? s=mid+1 : e=mid-1 -> 1,2 반복
           중앙값 == x, 탐색 성공 -> 1출력
        3. s = e가 되면 반복 종료
    3. M개의 정수를 모두 탐색할 떄까지 2 반복.
 */
public class 백준1920_정수찾기_이진탐색 {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i=0; i<N; i++){
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);

        int M = sc.nextInt();
        for (int i=0; i<M; i++){
            int target = sc.nextInt();
            int s = 0;
            int e = N-1;
            boolean find = false;
            while (s <= e) {
                int mid_idx = (s+e)/2;
                int mid_value = A[mid_idx];
                if (target == mid_value) {
                    find = true;
                    break;
                } else if (target < mid_value) {
                    e = mid_idx-1;
                } else {
                    s = mid_idx+1;
                }
            }
            if(find) System.out.println(1);
            else System.out.println(0);
        }
    }
}
