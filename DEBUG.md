## 2025-04-26

- This is a known issue about `charmap`
```
UnicodeEncodeError: 'charmap' codec can't encode character '\u010d' in position 55: character maps to <undefined>
```
- ( 2025-04-26 10:52:36 )
- Steps to
```bash
jazzw@JazzBook:~/git/confluence-insight$ bin/sample-run.sh BIGTOP
[INFO] storage_state.json found. loading into browser context.
[INFO] storage_state.json found. loading into browser context.
[INFO] storage_state.json found. loading into browser context.
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="gunnar.schroeder@tu-dresden.de">
<img alt="User icon: gunnar.schroeder@tu-dresden.de" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="gunnar.schroeder@tu-dresden.de"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (gunnar.schroeder@tu-dresden.de)</span></span> 
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="gunnar.schroeder@tu-dresden.de">
<img alt="User icon: gunnar.schroeder@tu-dresden.de" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="gunnar.schroeder@tu-dresden.de"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (gunnar.schroeder@tu-dresden.de)</span></span> 
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="konstantiniboudnik">
<img alt="User icon: konstantiniboudnik" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="konstantiniboudnik"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (konstantiniboudnik)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="rpelavin">
<img alt="User icon: rpelavin" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="rpelavin"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (rpelavin)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="rpelavin">
<img alt="User icon: rpelavin" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="rpelavin"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (rpelavin)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="rpelavin">
<img alt="User icon: rpelavin" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="rpelavin"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (rpelavin)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="rpelavin">
<img alt="User icon: rpelavin" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="rpelavin"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (rpelavin)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="dmitri101">
<img alt="User icon: dmitri101" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="dmitri101"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (dmitri101)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="dmitri101">
<img alt="User icon: dmitri101" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="dmitri101"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (dmitri101)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="dmitri101">
<img alt="User icon: dmitri101" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="dmitri101"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (dmitri101)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="dmitri101">
<img alt="User icon: dmitri101" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="dmitri101"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (dmitri101)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="dmitri101">
<img alt="User icon: dmitri101" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="dmitri101"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (dmitri101)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="javacruft">
<img alt="User icon: javacruft" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="javacruft"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (javacruft)</span></span>
</div>
</td>
#Exception `AttributeError` ----------------------
<td class="contributors" style="white-space: normal;">
<div class="page-history-contributor-link" data-username="javacruft">
<img alt="User icon: javacruft" class="userLogo logo anonymous" src="/confluence/s/-e27bm1/8804/z1btw/_/images/icons/profilepics/anonymous.svg" title="javacruft"/> <span class="page-history-contributor-name"> <span class="unknown-user">Unknown User (javacruft)</span></span>
</div>
</td>
Traceback (most recent call last):
  File "C:\Users\jazzw\git\confluence-insight\get-pageHistories.py", line 65, in <module>
    print(pageId[2] + ";" + version + ";" + published + ";" + contributor_id + ";" + contributor_name, file = pageHistories)
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u010d' in position 55: character maps to <undefined>
[INFO] storage_state.json found. loading into browser context.
Traceback (most recent call last):
  File "C:\Users\jazzw\git\confluence-insight\get-pageLinks.py", line 63, in <module>
    df = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 1898, in _make_engine
    return mapping[engine](f, **self.options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 93, in __init__
    self._reader = parsers.TextReader(src, **kwds)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "parsers.pyx", line 574, in pandas._libs.parsers.TextReader.__cinit__
  File "parsers.pyx", line 663, in pandas._libs.parsers.TextReader._get_header
  File "parsers.pyx", line 874, in pandas._libs.parsers.TextReader._tokenize_rows
  File "parsers.pyx", line 891, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "parsers.pyx", line 2053, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 6339: invalid continuation byte
Traceback (most recent call last):
  File "C:\Users\jazzw\git\confluence-insight\gen-pageGraph.py", line 26, in <module>
    df = pd.read_csv(space_key+"_pageHistories.csv", sep=';')
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\readers.py", line 1898, in _make_engine
    return mapping[engine](f, **self.options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 93, in __init__
    self._reader = parsers.TextReader(src, **kwds)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "parsers.pyx", line 574, in pandas._libs.parsers.TextReader.__cinit__
  File "parsers.pyx", line 663, in pandas._libs.parsers.TextReader._get_header
  File "parsers.pyx", line 874, in pandas._libs.parsers.TextReader._tokenize_rows
  File "parsers.pyx", line 891, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "parsers.pyx", line 2053, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 6339: invalid continuation byte
jazzw@JazzBook:~/git/confluence-insight$
```
- 根據這段錯誤，應該是 Windows 上才會遇到。因為這裡用的 encoding 是 `CP1252` (出現在 `python\current\Lib\encodings\cp1252.py`)
  - https://g.co/gemini/share/cee50a958173
  > CP1252, also known as Windows-1252 or sometimes (incorrectly) as "ANSI," is a single-byte character encoding that was widely used by default in Microsoft Windows for Western European languages.
```bash

Traceback (most recent call last):
  File "C:\Users\jazzw\git\confluence-insight\get-pageHistories.py", line 65, in <module>
    print(pageId[2] + ";" + version + ";" + published + ";" + contributor_id + ";" + contributor_name, file = pageHistories)
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u010d' in position 55: character maps to <undefined>
```
- 解法：強迫在 `open()` 檔案時，加入 `encoding='utf-8'`，就能避開在 Windows 平台運行時遇到的寫檔/讀檔錯誤。（因為網頁內容多半是 `UTF-8`，若要把 `UTF-8` 字串寫到 `CP1252` 的話，就會遇到這種典型的字集錯誤。