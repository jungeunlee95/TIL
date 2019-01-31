# 16 homework

### 1

```sql
CREATE TABLE friends(
	id INTEGER,
    name TEXT,
    location TEXT
);
```



### 2

```sql
INSERT INTO TABLE
VALUES(1, "Justin", "Seoul");

INSERT INTO TABLE
VALUES(2, "Simon", "New York");

INSERT INTO TABLE
VALUES(3, "Chang", "Las Vegas");

INSERT INTO TABLE
VALUES(4, "John", "Sydney");
```



### 3

```sqlite
ALTER TABLE friends
ADD married	INTEGER;
```



### 4

```sql
INSERT INTO TABLE(married)
VALUES(1)
WHERE id = 1;

INSERT INTO TABLE(married)
VALUES(0)
WHERE id = 2;

INSERT INTO TABLE(married)
VALUES(0)
WHERE id = 3;

INSERT INTO TABLE(married)
VALUES(1)
WHERE id = 4;
```



### 5

```sql
DELETE FROM friends
WHERE married = 0;
```



### 6

`DROP TABLE friends;`