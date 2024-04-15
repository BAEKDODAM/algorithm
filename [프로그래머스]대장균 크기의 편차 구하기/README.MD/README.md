# [프로그래머스 lv2] 연도별 대장균 크기의 편차 구하기 (SQL)

## 문제

[](https://school.programmers.co.kr/learn/courses/30/lessons/299310)

### 테이블

`ECOLI_DATA` 테이블

- 실험실에서 배양한 대장균들의 정보를 담은 테이블

| Column name | Type | Nullable |  |
| --- | --- | --- | --- |
| ID | INTEGER | FALSE | 대장균 개채 ID |
| PARENT_ID | INTEGER | TRUE | 부모 개체의 ID |
| SIZE_OF_COLONY | INTEGER | FALSE | 개체의  크기 |
| DIFFERENTIATION_DATE | DATE | FALSE | 분화되어 나온 날짜 |
| GENOTYPE | INTEGER | FALSE | 개체의 형질 |

### 문제

분화된 연도(`YEAR`), 분화된 연도별 대장균 크기의 편차(`YEAR_DEV`), 대장균 개체의 ID(`ID`) 를 출력하는 SQL 문을 작성해주세요.

- 분화된 연도별 대장균 크기의 편차 = 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기
- 결과는 연도에 대해 오름차순으로 정렬하고 같은 연도에 대해서는 대장균  크기의 편자에 대해 오름차순으로 정렬

## 풀이

### with문 사용

with문을 사용하여 좀 더 가독성 좋은 코드 작성

1. WITH절에서 연도별 MAX크기 구하기,
2. 연도를 기준을 JOIN하여 편차 구하기(연도별 최대값 - 각 레코드의 크기)

```sql
WITH MAX_SIZE AS (
	SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, 
				 MAX(SIZE_OF_COLONY) AS MAX_SIZE
	FROM ECOLI_DATA
	GROUP BY YEAR
)

SELECT M.YEAR,
			 (MAX_SIZE - E.SIZE_OF_COLONY) AS YEAR_DEV, 
			 ID
FROM ECOLI_DATA E
LEFT JOIN MAX_SIZE M 
		ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR
ORDER BY M.YEAR, YEAR_DEV
```

### with문 사용x

```sql
SELECT M.YEAR,
	   (MAX_SIZE - E.SIZE_OF_COLONY) AS YEAR_DEV, 
	   E.ID
FROM ECOLI_DATA E
	JOIN (
			SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, 
           MAX(SIZE_OF_COLONY) AS MAX_SIZE
			FROM ECOLI_DATA
			GROUP BY YEAR
	) M
	ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR
ORDER BY M.YEAR, YEAR_DEV
```

WITH문 관련 포스팅

[[SQL] WITH문](https://www.notion.so/SQL-WITH-e2447938d52a421688e8d3dab126e6a3?pvs=21)