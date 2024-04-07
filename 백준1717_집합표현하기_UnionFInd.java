import java.util.Scanner;
/*
    Q.
    {0},{1},{2},...{n} 초기에 집합이 있음
    합집합 연산과 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산 수행

    입력. 첫 줄에 원소 개수 n과 질의 개수 m 입력
    - 1<=n<=1,000,000, 1<=m<=100,000 입력. m은 연산 횟수
    - 0 a b 형태 -> 합집합(Union)
    - 1 a b 형태 -> 두 원소가 같은 집합에 포함되어 있는지 확인
    - 0 <= a, b <= n

    풀이
    수가 큼 -> 경로 압축이 필요한 Unoin-find 문제임 **
 */
/*
    Union-find
    1. 처음에는 노드가 연결x -> 각 노드의 대표노드 = 자기자신 -> 각 노드의 값을 인덱스 값으로 초기화
    2. find 연산으로 특정 대표 노드를 찾고, union 연산으로 2개의 노드를 이용해 각 대표 노드찾아 연결
       -> 질의한 값에 따라 결과 반환 (대표 노드를 다시 정하고 대표노드 값으로 노드 값 변경)
    주의할점* find 연산을 수행할 때 재귀 함수에서 나오면서 탐색한 모든 노드의 대표 노드값을 이번 연산에서 발견한 대표 노드로 변경하는 부분
             union 연산에서 선택된 노드끼리 연결하는 것이 아닌 선택된 노드의 대표 노드끼리 연결하는 부분
 */
public class 백준1717_집합_표현하기_UnionFind {
    static int parent[];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N= sc.nextInt();
        int M = sc.nextInt();
        parent = new int[N+1];
        for(int i=0; i<N+1; i++){ // 대표노드를 자기 자신으로 초기화
            parent[i] = i;
        }

        // 질의 처리
        for (int i =0; i<M; i++){
            int question = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(question == 0){ // union: 합집합 수행
                union(a,b);
            } else { // 두 원소 같은 집합인지 확인
                boolean result = checksum(a, b);
                if(result){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
    }
    private static void union(int a, int b){
        a = find(a); // *대표노드를 찾아서 연결해주기 위함*
        b = find(b);
        if(a!=b) {
            parent[b] = a; // 두 배열 연결(b의 대표노드를 a로 변경)
        }
    }
    private static int find(int a){
        if(a == parent[a]) return a; // 자기자신이 대표노드인지 확인
        else {  // 대표노드 찾아감
            return parent[a] = find(parent[a]); // 대표노드를 index로 바꿔서 또 찾아감 & *대표노드 변경(경로압축)*
        }
    }
    private static boolean checksum(int a, int b){ // 두 원소가 같은 집합인지 확인하고 리턴해주는 함수
        a = find(a);
        b = find(b);
        if(a==b) return true;
        return false;
    }
}
