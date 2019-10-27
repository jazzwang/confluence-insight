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

由於過去寫慣了 Shell Script，所以很多時候構思小型專案的時候，都會有點遵循 Linux 指令背後的思維，
一個階段/一個 State/一個目的就寫成一個指令。
優點是容易除錯，缺點是等到整個功能做得差不多了，又得再重構一次。另一個缺點是別人不容易看懂程式碼的結構。
像是需要把儲存成不同 CSV 的部分重新整理成合適的 Data Model，把重複的程式碼改用物件導向的方式設計。

反思：從構思，驗證，重構，再重新設計，這樣的迭代也許蠻花時間的，但也算是一種訓練啦～
回過頭去想底層的 Data Model 怎樣才精簡，怎麼減少運算步驟，
實際體驗一下不同的函式庫 BeautifulSoup, Selenium, pandas, networkx, webweb, etc.
也學著去從函示庫的原始碼學著寫得更模組化。

先前在分析臉書資料時，會用 [Gephi](https://gephi.org/) 來做 Social Network Analysis
感覺 networkx, webweb, plotly 的 dash 這幾個函式庫，提供了更多彈性。

也在看這些函示庫的範例過程中，學到 [requirements.txt](https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e) 跟 [Procfile](https://devcenter.heroku.com/articles/python-gunicorn) 的用法。

後續也許會再花點時間來看一下 [Pytest](https://docs.pytest.org/en/latest/) 跟 Github CI 的設定。