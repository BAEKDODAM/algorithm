import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
/*
    Q. 각 집합에 속한 노드끼리 서로 인접하지 않는 두 집합으로 그래프의 노드를 나눌 수 있는지 여부 판별

    입력. 첫 줄에 테스트 케이스 수 K
         테스트 케이스이 그래프 노드 개수 V, 그래프  에지 개수 E
         E개 줄에 걸쳐 엦 관련 정보(인접한 두 노드 번호)
         ...

    풀이. DFS 사용
        1. 그래프를 인접 리스트로 구현
        2. 모든 노드로 각각 DFS 사용해 탐색 수행
           방문한 노드이면, 이분그래프 아님
           만약 방문하지 않은 노드이면, 현재 노드와 다른 집합으로 연결 노드 집합 저장
           dfs 실행(재귀)
 */
public class 백준1707_이분그래프_판별_DFS {
    static ArrayList<Integer>[] A;
    static int[] check;
    static boolean[] visited;
    static boolean isEven;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine()); // 테스트 케이스 개수
        for (int t=0; t<testCase; t++){
            String[] s = br.readLine().split(" ");
            int V = Integer.parseInt(s[0]); // 노드 개수
            int E = Integer.parseInt(s[1]); // 에지 개수

            A = new ArrayList[V+1];
            check = new int[V+1];
            visited = new boolean[V+1];
            isEven= true;
            for (int i=1; i<=V; i++){
                A[i] =  new ArrayList<Integer>();
            }

            // 에지 데이터 저장하기
            for(int i=0; i<E; i++){
                s = br.readLine().split(" ");
                int start = Integer.parseInt(s[0]);
                int end = Integer.parseInt(s[1]);

                A[start].add(end);
                A[end].add(start);
            }
            // 모든 노드에서 dfs 실행 해야함
            for (int i=1; i<=V; i++){
                if (isEven) { // 이분그래프인 경우만 DFS 실행
                    DFS(1);
                }else break;
            }
            if(isEven) System.out.println("YES");
            else System.out.println("NO");
        }
    }
    private static void DFS(int start){
        visited[start]=true;
        for (int i: A[start]){
            if (!visited[i]){
                check[i] = (check[start]+1)%2; // 직전 값이 1이었으면 0, 0이었으면 1이 들어감
                DFS(i);
            } else if(check[start] == check[i]){
                isEven = false;
            }
        }
    }
}
