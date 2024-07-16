-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE 
FROM BOOK
WHERE CATEGORY LIKE '인문' and PUBLISHED_DATE LIKE '2021%'
ORDER BY PUBLISHED_DATE ASC;