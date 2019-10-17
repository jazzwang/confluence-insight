```
sample-output$ sqlite3 hadoop.db
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> create table "pageHistories" (
   ...>  pageId int,
   ...> version int,
   ...> published timestamp,
   ...> user_id varchar,
   ...> user_name varchar
   ...> );
sqlite> .mode csv
sqlite> .separator ';'
sqlite> .import pageHistories.csv pageHistories
sqlite> select user_id, pageId, count(published) from pageHistories group by user_id, pageId;
```