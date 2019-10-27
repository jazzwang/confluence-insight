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
## Generate Graph via Python

### Reading List

* Social Network Analysis
    * https://www.datacamp.com/community/tutorials/social-network-analysis-python
    * https://github.com/briatte/awesome-network-analysis#python
* Pandas: SQL
    * https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
* Pandas: CSV
    * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
* Pandas: CSV -> unique (distinct)
    * https://www.geeksforgeeks.org/getting-unique-values-from-a-column-in-pandas-dataframe/
* Pandas: CSV -> group by
    * https://www.geeksforgeeks.org/pythonp-pandas-dataframe-groupby/
    * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

### Network Graph Implementation

* https://snap.stanford.edu/
* https://github.com/dblarremore/webweb
* https://networkx.github.io/
* https://plot.ly/python/network-graphs/
    * https://dash.plot.ly/

## 心得/設計思路

記錄一下心得與設計思路。
由於過去寫慣了 Shell Script，所以很多時候構思小型專案的時候，都會有點遵循 Linux 指令背後的思維，一個階段/一個 State/一個目的就寫成一個指令。
優點是容易除錯，缺點是等到整個功能做得差不多了，又得再重構一次。像是需要把儲存成不同 CSV 整理成合適的 Data Model，把重複的程式碼改用物件導向的方式設計。