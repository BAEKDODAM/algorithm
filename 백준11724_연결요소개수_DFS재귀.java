import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/*
    DFS = stack
    인접리스트에 노드와 에지 연결 정보 저장
    노드 1부터 시작
    방문 확인 -> 방문했으면 return = 하나의 연결된 덩어리가 끝난 것임
             -> 방문 안했으면 인접한 리스트 방문
 */

public class 백준11724_연결요소개수_DFS재귀 {
    static boolean[] visited;
    static ArrayList<Integer>[] A; // 미로
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        A = new ArrayList[N+1];
        for (int i=1; i<N; i++){
            A[i] = new ArrayList<>();
        }
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            A[s].add(e);
            A[e].add(s);
        }
        int cnt = 0;
        for(int i=1; i<N+1; i++){
            if(!visited[i]){
                cnt++;
                DFS(i);
            }
        }
        System.out.println(cnt);
    }

    public static void DFS(int v){
        if(visited[v]) return;
        visited[v]=true;
        for (int i : A[v]){
            DFS(i);
        }
    }
}
/*
    Q. 노드 개수 N, 에지 개수 M
    1<=N<=1,000 0<=M<=N*(N-1)/2
    M개의 줄에 에지의 양끝 점 u, v 주어짐. 같은 에지는 한 번만 주어짐

    풀이.
    O(n^)도 가능
    한 번의 dfs가 끝날 때까지 탐색한 모든 노드 집합이 하나의 연결 요소
    1. 인접리스트 생성해 입력받은 값 넣기
    2. 1부터 시작해 인접한 곳 방문, 방문 배열에 방문 표시
    3. 반복해서 방문
    4. dfs 끝나면 cnt++
    5. 다음 노드 2-4 반복
    6. 모두 방문하면 종료
 */