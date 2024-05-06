import java.util.Scanner;

public class 백준2018_연속된_자연수_합_투포인터 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);
        int N = sc.nextInt();
        int cnt = 1;
        int startIndex  = 1;
        int endIndex = 1;
        int sum = 1;
        while(endIndex !=N ){
            if (sum == N) {
                cnt++; endIndex++;  sum+=endIndex;
            } else if (sum > N) {
                sum -= startIndex;
                startIndex++;
            } else {
                endIndex++;
                sum += endIndex;
            }
        }
        System.out.println(cnt);
    }
}
/*
    문제: 입력받은 자연수(N)를 연속된 자연수의 합으로 나타낼 수 있는 가지수 출력
    조건: 1<=N<=10,000,000 (천만)
    -> O(nlogn)도 위험.. O(n) 사용 -> 투포인터 사용!

    풀이 방법: * 투포인터 *
    1. 배열의 하나의 인덱스를 가리키는 Start 점과 End 점 두 개를 만들자.(start는 시작 지점, End는 끝점을 가리킨다.)
    2. 처음 start와 end는 0으로 초기화해준다.
    3. start 점부터 end점까지의 합을 구해서 sum에 저장해준다. (처음 sum은 0에서 0까지니까 배열의 0번째 인덱스 값이 저장된다.)
    4. 배열을 도는데 세 가지 조건으로 돈다.
        1. sum == 찾고자 하는 값 --> 값을 만족하는 구간을 찾았으니 cnt(카운트 개수)를 하나 늘려주고, sum의 값에서 start인덱스의 값을 빼주고 1을 늘려준다. 그리고 end값을 1을 더한 후 그 인덱스의 값을 sum에 더해준다. (말이 좀 복잡한데 직접 문제를 생각해보면 뭔 말인지 이해할 것이다.)
        2. sum < 찾고자 하는 값 --> sum이 더 작으니까 값을 늘려주어야 한다. start 값은 그대로 두고, end 값을 1 늘려주고 그 end 인덱스의 값을 sum에 더해준다.
        3. sum > 찾고자 하는 값 --> sum이 더 크니까 값을 줄여주어야 한다. end 값은 그대로 두고, start 인덱스 값을 sum에서 빼주고 start값을 1 늘려서 갱신해준다.
    5. 루프를 탈출하는 경우는 start 값이나 end 값이 배열의 인덱스를 초과하면 예외처리를 통해 탈출한다.(이 방법은 권장하지 않으니 다른 방법을 생각해보기 바란다.)
 */