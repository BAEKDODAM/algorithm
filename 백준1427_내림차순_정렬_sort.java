import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class 백준1427_내림차순_정렬_sort {
    public static void main(String[] args) throws IOException {
        Scanner sc =   new Scanner(System.in);
        String str = sc.next();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N을 자릿수별로 나눔
        char[] arr = br.readLine().toCharArray();

        // 정렬
        Arrays.sort(arr);

        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i]);
        }

        //-------------------------------

        int A[] = new int[str.length()];
        for (int i=0; i<str.length(); i++){
            A[i] = Integer.parseInt(str.substring(i,i+1));
        }
        //선택 정렬
        for(int i=0; i<str.length(); i++){
            int Max = i;
            for(int j = i+1; j<str.length(); j++){
                if(A[j]>A[Max]) {
                    Max = j;
                }
            }
            if(A[i] < A[Max]){
                int temp = A[i];
                A[i] = A[Max];
                A[Max] = temp;
            }
        }
    }
}
/*
    Q. 수가 주어지면 그 수의 각 자릿수를 내림차순으로 정렬
    N <= 1,000,000,000
 */