import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/*
    <큐 사용법>
                    예외 발생      값 리턴
    추가(enqueue)	add(e)       offer(e)
    삭제(dequeue)	remove()	 poll()
    검사(peek)	    element()	 peek()

    Q. N*M 미로에서 1은 갈 수 있고 0은 갈 수 없음
    (0,0)에서 (N,M)으로 가는 최단경로 찾기
    2<=N,M<=100

    풀이. BFS 또는 DFS 사용
    DFS는 깊이를 저장하고 있으며 끝까지 내려감 - 어렵
    BFS
 */
public class 백준2178_미로탐색_BFS {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static boolean[][] visited;
    static int[][] A; // 데이터 저장하는 2차원 배열
    static int N, M; // row, column

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            String line = st.nextToken();
            for (int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(line.substring(j, j + 1));
            }
        }
        BFS(0, 0);
        System.out.println(A[N-1][M-1]);
    }

    public static void BFS(int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{i, j});
        while (!queue.isEmpty()) {
            int now[] = queue.poll();
            visited[i][j] = true;
            for (int k = 0; k < 4; k++) { // 상하좌우 탐색
                int x = now[0] + dx[k];
                int y = now[1] + dy[k];
                if (x >= 0 && y >= 0 && x < N && y < M) { // 배열을 넘어가면 안되고
                    if (A[x][y] != 0 && !visited[x][y]) { //  0이어서 갈 수 없거나 기방문한 곳이면 안됨
                        visited[x][y] = true;
                        A[x][y] = A[now[0]][now[1]] + 1; // 중요* 깊이 넣음
                        queue.add(new int[]{x, y});
                    }
                }
            }
        }
    }
}
