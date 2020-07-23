SELECT * INTO keyword_copy FROM keyword WHERE 1 = 0;

INSERT INTO keyword_copy SELECT id, keyword, country, type FROM keyword GROUP BY keyword, country;

truncate table keyword;

set @n = 0;
INSERT INTO keyword SELECT (@n := @n + 1) as id, keyword, country, type FROM keyword_copy;

DROP TABLE keyword_copy;