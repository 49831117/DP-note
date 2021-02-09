# Web Crawler - 基礎

----
## 入門
### HTML
HyperText Markup Language
- 標籤（tags），如：`<p>`、`</p>`
- 屬性（Attributes），如：`<img>` 的 `src`、`width`、`height`
  `<img scr="sample.jpg" width="20" height="30">`
- HTML5 支援跨平台，擴充及改進 HTML 標籤和 API。
    ```html
    <!DOCTYPE html>
    <html lang="zh">
    <head>  
    <meta charset="utf-8">
    <title>網頁標題文字</title>
    </head>
    <body>網頁的結構
    網頁內容
    </body>
    </html>
    ```
- XML 非取代 HTML，描述資料用。補足 HTML 標籤的不足，更有擴充性

### JSON
JavaScript Object Notation
- 取得的網路資料除了自行從HTML標籤取得，亦可透過AJAX下載JSON格式文件
- 和 python 的字典相似
  - 以鍵值對方式表示
    - 值：整數、浮點數、字串、布林值、陣列、物件
  - 使用大括號定義物件
  - 使用方括號定義物件陣列

```json
{
    "Boss": "陳會安",
    "Employees": [
    { "name" : "陳允傑", "tel" : "02-22222222" },
    { "name" : "江小魚", "tel" : "02-33333333" },
    { "name" : "陳允東", "tel" : "04-44444444" }
    ]
}
```


## What's web crawler？
### 用途

### 步驟
1. 目標 URL 網址
   ```python
    import urllib.request as request
    with request.urlopen(網址) as response:
       data = response.read()
    print(data)
   ```
   1. 適合的資料來源：[台北市政府公開資料](http://data/taipei/)
2. 送出 request 取得網頁
3. 分析網頁
   1. 確認資料格式：JSON、CSV...等
    ```python
    import urllib .request as request
    src="https://www.cjcu.edu.tw/"
    with request.urlopen(src)as response:
        data=response.read() #取得長榮大學網站的原始碼(HTML、CSS、JASON)
        print(data)
    with request.urlopen(src)as response:
        data=response.read().decode("utf-8") #utf-8解碼
    print(data)
    ```
4. 取出所需資料

### 相關函式庫
- 靜態網頁
  1. Beautiful Soup
  2. lxml
- 動態網頁
  1. Selenium
  2. WebDriver
- 爬取整個網站
  1. Scrapy 網路爬蟲框架幫助建立 python 爬蟲程式

