# [프로그래머스 Lv2] 특정 물고기를 잡은 총 수 구하기 (SQL)

## 문제

[[프로그래머스 Lv2] 특정 물고기를 잡은 총 수 구하기 (SQL)](https://school.programmers.co.kr/learn/courses/30/lessons/298518)

### 테이블

- `FISH_INFO` 테이블 : 잡은 물고기 정보 담음
    - `FISH_INFO` 테이블 구조 : `ID`, `FISH_TYPE`, `LENGTH`, `TIME`
    
    | Column name | Type | Nullable |
    | --- | --- | --- |
    | ID | INTEGER | FALSE |
    | FISH_TYPE | INTEGER | FALSE |
    | LENGTH | FLOAT | TRUE |
    | TIME | DATE | FALSE |
    - 단, 잡은 물고기의 길이가 10cm 이하일 경우에는 `LENGTH` 가 NULL 이며, `LENGTH` 에 NULL 만 있는 경우는 없습니다.
- `FISH_NAME_INFO` 테이블 : 물고기의 이름에 대한 정보를 담음
    - `FISH_NAME_INFO` 테이블 구조: `FISH_TYPE`, `FISH_NAME`
    
    | Column name | Type | Nullable |
    | --- | --- | --- |
    | FISH_TYPE | INTEGER | FALSE |
    | FISH_NAME | VARCHAR | FALSE |

### 문제

`FISH_INFO` 테이블에서 잡은 `BASS`와 `SNAPPER`의 수를 출력하는 SQL 문을 작성해주세요.

컬럼명은 'FISH_COUNT`로 해주세요.

## 풀이

- JOIN 사용해서 두 테이블 합침
- WHERE 사용해서 조건에 맞는 행만 추림
- COUNT 사용해서 수만 출력
- AS 사용해서 컬럼명 지정

```sql
SELECT COUNT(*) AS FISH_COUNT 
FROM FISH_INFO AS I
JOIN FISH_NAME_INFO AS N
ON I.FISH_TYPE = N.FISH_TYPE
WHERE N.FISH_NAME IN ('BASS','SNAPPER');
```