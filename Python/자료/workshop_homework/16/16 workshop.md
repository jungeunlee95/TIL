# 16 workshop



### 1

```sqlite
ALTER TABLE bands
ADD members INTEGER;
```



### 2

```sqlite
INSERT INTO TABLE(members)
VALUES(4)
WHERE id = 1;

INSERT INTO TABLE(members)
VALUES(5)
WHERE id = 2;

INSERT INTO TABLE(members)
VALUES(9)
WHERE id = 3;

```



### 3

```sqlite
UPDATE bands 
SET members = 5
WHERE id = 3;
```



### 4

```sqlite
DELETE FROM bands
WHERE id = 2;
```

