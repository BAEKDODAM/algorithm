import java.util.Scanner;
/*
    Q. 수식에 괄호들을 추가해서 최솟값 만들기

    풀이.
    빼는 숫자가 크면 클수록 전체 수식의 결과는 최소가 됨
    들어오는 데이터를 -를 기준으로 split
    for(각 나눠진 데이터 개수만큼){
        나눠진 데이터 연산 실행하는 함수 mySum() 호출
        if(가장 앞 데이터면) answer에 결괏값 더하기
        else answer에 결괏값 빼기
    }
    answer 출력
    mySum(String s){
        s를 +기준으로 split
        for(나눈 만큼) integer로 변환해서 더하기
    }
 */
public class 백준1541_최솟값괄호배치_그리디 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String cal = sc.nextLine();
        String[] str = cal.split("-");
        int answer = 0;
        for (int i=0; i<str.length; i++){
            int temp = mySum(str[i]);
            if (i==0) answer+=temp;
            else answer -= temp;
        }
    }
    private static int mySum(String s) {
        int sum = 0;
        String[] temp = s.split("[+]");// +는 인식을 잘 못함 -> [+]로 바꾸기!
        for(int i=0; i< temp.length; i++){
            sum += Integer.parseInt(temp[i]);
        }
        return sum;
    }
}
