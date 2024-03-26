## 문제

[[프로그래머스 Lv1] 가장 큰 물고기 10마리 구하기 (SQL)](https://school.programmers.co.kr/learn/courses/30/lessons/298517)

### 테이블

- `FISH_INFO` 테이블: 잡은 물고기 정보 담
    
    
    | Column name | Type | Nullable |
    | --- | --- | --- |
    | ID | INTEGER | FALSE |
    | FISH_TYPE | INTEGER | FALSE |
    | LENGTH | FLOAT | TRUE |
    | TIME | DATE | FALSE |
    - 단, 잡은 물고기의 길이가 10cm 이하일 경우에는 `LENGTH` 가 NULL 이며, `LENGTH` 에 NULL 만 있는 경우는 없습니다.

### 문제

`FISH_INFO` 테이블에서 가장 큰 물고기 10마리의 ID와 길이를 출력하는 SQL 문을 작성해주세요. 

결과는 길이를 기준으로 내림차순 정렬하고, 길이가 같다면 물고기의 ID에 대해 오름차순 정렬해주세요. 

단, 가장 큰 물고기 10마리 중 길이가 10cm 이하인 경우는 없습니다.

ID 컬럼명은 `ID`, 길이 컬럼명은 `LENGTH`로 해주세요.

</br>

## 풀이

- SELECT 할 때 ID와 LENGTH만 출력하도록 함
- **ORDER BY**를 사용하여 LENGTH 내림차순(**DESC**)으로 정렬하고 다음으로 ID 오름차순으로 정렬하도록 함
- **LIMIT** 사용하여 지정한 갯수(10개)만큼의 행만 출력

```sql
SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID
LIMIT 10;
```