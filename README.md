# e2e-tests-asyncio

## Create table

```
create table cart_log (
   id INT NOT NULL AUTO_INCREMENT,
   merchant_id VARCHAR(32) NOT NULL,
   logged DATE,
   PRIMARY KEY ( id )
);
```

## Insert record

```
INSERT INTO cart_log VALUES (8, '123', NOW())
```
