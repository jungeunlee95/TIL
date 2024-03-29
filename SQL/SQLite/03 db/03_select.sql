--1. 상시간이 150분 이상인 영화이름만 출력하세요. 
SELECT 영화이름 FROM movies
WHERE 상영시간 > 150;

--2. 장르가 애니메이션인 영화코드와 영화이름를 출력하세요. 
SELECT 영화코드, 영화이름 FROM movies
WHERE 장르 > "애니메이션";

--3. 제작국가가 덴마크이고 장르가 애니메이션인 영화이름을 출력하세요. 
SELECT 영화이름 FROM movies
WHERE 제작국가 > "덴마크"
AND 장르="애니메이션";

--4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수를 출력하세요. 
SELECT 영화이름, 누적관객수 FROM movies
WHERE 누적관객수 > 1000000
AND 관람등급="청소년관람불가";

--5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화를 출력하세요. 
SELECT 영화이름,개봉연도 FROM movies
WHERE 개봉연도 BETWEEN 20000101 AND 20091231;

--6. 장르를 중복 없이 출력하세요
SELECT 장르 FROM movies
GROUP BY 장르;