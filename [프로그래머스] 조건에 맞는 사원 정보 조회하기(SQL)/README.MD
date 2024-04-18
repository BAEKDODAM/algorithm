# [프로그래머스 lv2] 조건에 맞는 사원 정보 조회하기(SQL)

태그: Database
날짜: 2024년 4월 18일 오후 3:28

## 문제

[](https://school.programmers.co.kr/learn/courses/30/lessons/284527)

### 테이블

- `HR_DEPARTMENT` 테이블: 회사의 부서 정보를 담은 테이블
    
    
    | Column name | Type | Nullable | 의미 |
    | --- | --- | --- | --- |
    | DEPT_ID | VARCHAR | FALSE | 부서ID |
    | DEPT_NAME_KR | VARCHAR | FALSE | 국문 부서명 |
    | DEPT_NAME_EN | VARCHAR | FALSE | 영문 부서명 |
    | LOCATION | VARCHAR | FLASE | 부서 위치 |
- `HR_EMPLOYEES` 테이블: 회사의 사원 정보를 담은 테이블
    
    
    | Column name | Type | Nullable | 의미 |
    | --- | --- | --- | --- |
    | EMP_NO | VARCHAR | FALSE | 사번 |
    | EMP_NAME | VARCHAR | FALSE | 성명 |
    | DEPT_ID | VARCHAR | FALSE | 부서 ID |
    | POSITION | VARCHAR | FALSE | 직책 |
    | EMAIL | VARCHAR | FALSE | 이메일 |
    | COMP_TEL | VARCHAR | FALSE | 전화번호 |
    | HIRE_DATE | DATE | FALSE | 입사일 |
    | SAL | NUMBER | FALSE | 연봉 |
- `HR_GRADE` 테이블: 2022년 사원의 평가 정보를 담은 테이블
    
    
    | Column name | Type | Nullable | 의미 |
    | --- | --- | --- | --- |
    | EMP_NO | VARCHAR | FALSE | 사번 |
    | YEAR | NUMBER | FALSE | 연도 |
    | HALF_YEAR | NUMBER | FALSE | 반기 |
    | SCORE | NUMBER | FALSE | 평가 점수 |

### 문제

`HR_DEPARTMENT`, `HR_EMPLOYEES`, `HR_GRADE` 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회하려 합니다. 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회하는 SQL문을 작성해주세요.

2022년도의 평가 점수는 상,하반기 점수의 합을 의미하고, 평가 점수를 나타내는 컬럼의 이름은 `SCORE`로 해주세요.

## 풀이

1. WITH 사용해 HR_GRADE에서 각 사원의 인사점수 합 배열(SUM_SCORE) 만들기
2. 점수, 사번, 성명, 직책, 이메일은 HR_EMPLOYEES 테이블과 JOIN 해서 가져오기
3. SUM_SCORE의 SCORE가 가장 높은 사원 출력

```sql
WITH SUM_SCORE AS (
	SELECT EMP_NO, SUM(SCORE) AS SCORE
	FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT S.SCORE AS SCORE, E.EMP_NO AS EMP_NO, EMP_NAME, POSITION, EMAIL
FROM  HR_EMPLOYEES E
JOIN SUM_SCORE S
ON E.EMP_NO = S.EMP_NO
WHERE SCORE = (SELECT MAX(SCORE) FROM SUM_SCORE)
```