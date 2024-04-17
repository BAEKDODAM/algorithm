# [프로그래머스 lv1] 한 해에 잡은 물고기 수 구하기(SQL)

태그: Database
날짜: 2024년 4월 17일 오후 9:01

## 문제

[](https://school.programmers.co.kr/learn/courses/30/lessons/298516)

### 테이블

FISH_INFO

| Column name | Type | Nullable | 의미 |
| --- | --- | --- | --- |
| ID | INTEGER | FALSE | 물고기의 ID |
| FISH_TYPE | INTEGER | FALSE | 물고기의 종류(숫자) |
| LENGTH | FLOAT | TRUE | 잡은 물고기의 길이(cm) |
| TIME | DATE | FALSE | 물고기를 잡은 날짜 |
- 잡은 물고기의 길이가 10cm 이하일 경우에는 `LENGTH` 가 NULL 이며, `LENGTH` 에 NULL 만 있는 경우는 없습니다.

### 문제

FISH_INFO 테이블에서 2021년도에 잡은 물고기 수를 출력하는 SQL 문을 작성해주세요.

이 때 컬럼명은 'FISH_COUNT' 로 지정해주세요.

## 풀이

1. COUNT 사용하여 물고기 수 세기
2. DATE 자료형에서 년도 정보만 필요할 때는 YEAR() 사

```sql
SELECT COUNT(*) AS FISH_COUNT 
FROM FISH_INFO
WHERE YEAR(TIME) = 2021
```