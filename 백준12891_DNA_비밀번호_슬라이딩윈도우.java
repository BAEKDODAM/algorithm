import javax.xml.transform.Result;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
    슬라이딩 윈도우
    - 두 개의 포인터로 범위를 지정한 다음 범위를 유지한 채로 이동

    문제:
    {'A','C','G','T'}로 구성된 길이가 S인 문자열에서
    길이가 P이고 각 문자 개수가 특정 개수 이상인 부분 뽑아서 비밀번호 만들음
    가능한 비밀번호 수 출력

    조건: 1<=|P|<=|S|<=1,000,000 백만

    풀이:
    슬라이딩 윈도우 사용
    1. i ~ i+P-1 을 자름 (i=0; i<S-P+1; i++)
    2. 개수 조건 만족하는지 확인
       i가 증가하면서 들어오는 값과 나가는 값만 확인하면 됨
    3. cnt++
 */

public class 백준12891_DNA_비밀번호_슬라이딩윈도우 {
    static int myArr[];
    static int checkArr[];
    static int checkSecret;
    public static void main(String[] args) throws IOException {
        BufferedReader bf =
                new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int S = Integer.parseInt(st.nextToken()); // 문자열 길이
        int P = Integer.parseInt(st.nextToken()); // 부분 문자열 길이
        int result = 0;
        checkArr = new int[4]; // dna 문자 조건 / 비밀번호 체크배열
        myArr =  new int[4]; // 현재 비밀번호 상태 배열
        char A[] = new char[S]; // dna 문자열
        A = bf.readLine().toCharArray();

        checkSecret = 0; // 지금 몇 개가 부분문자열 조건에 충족하는지
        //char[] c = {'A','C','G','T'};

        st = new StringTokenizer(bf.readLine()); // dna 문자가 각각 몇개 있어야 하는지 조건
        for (int i=0; i<4; i++){
            checkArr[i] = Integer.parseInt(st.nextToken());
            if(checkArr[i] == 0) checkSecret++; // 0이면 이미 조건 만족한 거니까
        }

        for (int i=0; i<P; i++) { // 부분문자열 처음 받을 때 세팅
            Add(A[i]);
        }
        if(checkSecret == 4) result++;

        // 슬라이딩 윈도우 시작
        for(int i=P; i<S; i++) { // i는 슬라이딩 윈도우의 가장 오른쪽 끝, j는 왼쪽 끝
            int j = i-P;
            Add(A[i]);
            Remove(A[j]);
            if(checkSecret == 4) result++;
        }
        System.out.println(result);
        bf.close();
    }

    public  static void Add(char c){
        switch (c) {
            case 'A':
                myArr[0]++;
                if(myArr[0] == checkArr[0]) checkSecret++;
                break;
            case 'C':
                myArr[1]++;
                if(myArr[1] == checkArr[1]) checkSecret++;
                break;
            case 'G':
                myArr[2]++;
                if(myArr[2] == checkArr[2]) checkSecret++;
                break;
            case 'T':
                myArr[3]++;
                if(myArr[3] == checkArr[3]) checkSecret++;
                break;
        }
    }

    public  static void Remove(char c){
        switch (c) {
            case 'A':
                if(myArr[0] == checkArr[0]) checkSecret--;
                myArr[0]--;
                break;
            case 'C':
                if(myArr[1] == checkArr[1]) checkSecret--;
                myArr[1]--;
                break;
            case 'G':
                if(myArr[2] == checkArr[2]) checkSecret--;
                myArr[2]--;
                break;
            case 'T':
                if(myArr[3] == checkArr[3]) checkSecret--;
                myArr[3]--;
                break;
        }
    }
}
