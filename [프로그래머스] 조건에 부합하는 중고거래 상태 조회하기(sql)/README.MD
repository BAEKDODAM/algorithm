# [프로그래머스 lv2] 조건에 부합하는 중고거래 상태 조회하기(sql)

태그: Database
날짜: 2024년 4월 19일 오후 12:22

## 문제

[[프로그래머스 lv2] 조건에 부합하는 중고거래 상태 조회하기(sql)](https://school.programmers.co.kr/learn/courses/30/lessons/164672)

### 테이블

`USED_GOODS_BOARD` 테이블: 중고거래 게시판 정보를 담은 테이블

| Column name | Type | Nullable | 의미 |
| --- | --- | --- | --- |
| BOARD_ID | VARCHAR(5) | FALSE | 게시글 id |
| WRITER_ID | VARCHAR(50) | FALSE | 작성자 ID |
| TITLE | VARCHAR(100) | FALSE | 게시글 제목 |
| CONTENTS | VARCHAR(1000) | FALSE | 게시글 내용 |
| PRICE | NUMBER | FALSE | 가격 |
| CREATED_DATE | DATE | FALSE | 작성일 |
| STATUS | VARCHAR(10) | FALSE | 거래상태 (SALE, RESERVED, DONE) |
| VIEWS | NUMBER | FALSE | 조회수 |

### 문제

USED_GOODS_BOARD 테이블에서 2022년 10월 5일에 등록된 중고거래 게시물의 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래상태를 조회하는 SQL문을 작성해주세요. 

거래상태가 SALE 이면 판매중, RESERVED이면 예약중, DONE이면 거래완료 분류하여 출력해주시고, 결과는 게시글 ID를 기준으로 내림차순 정렬해주세요.

## 풀이

1. CASE 사용하여 거래상태별로 분류하여 출력
2. WHERE절 사용해 2022년 10월 5일에 등록된 중고거래 게시물 필터링
3. ORDER BY 사용하여 게시글 ID 기준으로 내림차순 정렬

```sql
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, CASE STATUS
           WHEN 'SALE' THEN '판매중'
           WHEN 'RESERVED' THEN '예약중'
           WHEN 'DONE' THEN '거래완료'
           ELSE '알 수 없음'
       END AS STATUS
FROM USED_GOODS_BOARD
WHERE DATE(CREATED_DATE) = '2022-10-05'
ORDER BY BOARD_ID DESC;
```