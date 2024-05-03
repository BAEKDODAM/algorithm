import java.util.Scanner;
public class 백준1546_평균_구하기 {
    public static void main(String[] args) {
        // 최댓값 M, 모든 과목 -> 점수/M*100
        // 새로운 평균 구하기
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long sum = 0;
        long M = 0;

        for (int i=0; i<N; i++){
            int input = sc.nextInt();
            if (M < input) M = input;
            sum += input;
        }
        System.out.println(sum*100.0/M/N);
    }
}
/*
점수 최댓값 M, 모든 과목 점수 -> 점수/M*100
새로운 평균 구해 출력

최고점은 따로 저장해야함
수식으로 표현 -> (모든 점수 합)*(100/M)/N
 */