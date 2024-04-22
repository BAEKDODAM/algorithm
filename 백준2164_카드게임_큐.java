import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
/*
    <큐 사용법>
                    예외 발생      값 리턴
    추가(enqueue)	add(e)       offer(e)
    삭제(dequeue)	remove()	 poll()
    검사(peek)	    element()	 peek()
 */
public class 백준2164_카드게임_큐 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> myQueue = new LinkedList<>();

        int N = sc.nextInt();
        for(int i=1; i<=N; i++){
            myQueue.add(i);
        }

        while (myQueue.size()>1){
            myQueue.poll();
            myQueue.add(myQueue.poll());
        }
        System.out.println(myQueue.poll());
    }
}

/*
    문제:
    가장 위 카드 제거 -> 가장 위 카드 가장 아래로 이동 -> 한 장 남을 때까지 반복
    1<=N<=500,000
    마지만 남는 카드 출력

    풀아:
    큐 이용
    1. 모든 카드 큐에 담음
    2. queue.poll()
    3. queue.add(queue.poll())
 */