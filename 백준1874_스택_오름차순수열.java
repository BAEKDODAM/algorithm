import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

/*
  - Stack<Integer> stack = new Stack<>();
    stack.push(값);, stack.pop()

  - 여러 줄 출력 시 StringBuffer bf = new StringBuffer();에 담음
    bf.append(값);으로 추가
*/
public class 백준1874_스택으로_오름차순_수열_만들기 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A[] =  new int[N];
        for (int i=0; i<N; i++){
            A[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack<>();
        int num = 1; // 스택에 넣을 숫자 1~

        boolean result = true;

        StringBuffer bf = new StringBuffer();
        for (int i=0; i<A.length; i++) {
            int out = A[i]; // 현재 꺼내야하는 숫자
            if(out >= num) { // 꺼내야 하는 숫자가 스택에 넣을 숫자보다 크면 -> 스택에 숫자를 넣어줌
                while(out >= num){
                    stack.push(num++);
                    bf.append("+\n");
                }
                // 꺼내야 하는 숫자가 스택에 넣을 숫자보다 작아지면 pop
                stack.pop();
                bf.append("-\n");
            } else {
                int n = stack.pop();
                if(n>out) { // 꺼낼 숫자보다 pop한 숫자가 더 크면 순열을 완성될 수 없음
                    result = false;
                    System.out.println("NO");
                    break;
                } else {
                    bf.append("-\n");
                }
            }
        }
        if (result){
            System.out.println(bf.toString());
        }
    }
}

/*
    문제:
    수열을 스택에 넣었다가 출력하는 방식으로 오름차순 수열을 출력할 수 있는지 확인하고
    가능하면 push와 pop 연산을 어떤 순서로 수행해야 하는지를 알아내는 프로그램
    입력: 첫줄에 수열 개수 n, 두번째 줄~n번째 줄은 수열을 이루는 1이상 n이하의 정수
         이떄 같은 정수 안나옴
         1<=n<=100,000
    출력: 오름차순 수열을 만들기  위한 연산 순서 출력.
         push 연산은 +, pop 연산은 -, 불가능할 땐 NO

    풀이: 스택
    FILO 후입선출
 */

