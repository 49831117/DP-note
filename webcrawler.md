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
### 相關技術
### 相關函式庫
