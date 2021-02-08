# Pandas
結合了 series 和 DataFrame

----

- `pd.DataFrame(字典)` 以字典資料為底，建立 DataFrame
    ```python
    data = pd.DataFrame({
        "name" : ["May", "Lin", "Bob"]
        "salary" : [30000, 60000, 500000]
    })
    ```
- 取得特定欄
     ```python
    data = pd.DataFrame(字典)
    data["欄位名稱"]
    ```
- 取得特定列
    ```python
    data = pd.DataFrame(字典)
    data.iloc[列編號]
    ```
- `data = pd.Series([列表])`
- `data.max()`
- `data.median()`
- `data = data * 2`


## 資料處理

### Pandas 資料分析 - Series
- 單維度
- 建立 Seies
    ```python
    pd.Series([列表])
    ```
- 資料索引
    ```python
    pd.Series(資料列表)
    ```
- 自訂索引
    ```python
    pd.Series(資料列表, index = 索引列表)
    ```
- 觀察資料
  - 資料型態
        ```python
        data = pd.Series(資料列表)
        print(data.type)
        ```
  - 資料數量
        ```python
        data = pd.Series(資料列表)
        print(data.size)
        ```
  - 資料索引
        ```python
        data = pd.Series(資料列表, index = 索引列表)
        print(data.index)
        ```
  - 根據順序取值
        ```python
        data = pd.Series(資料列表)
        print(data[1]) # 印出 data 中的第一欄資料
        ```
  - 根據索引取值
        ```python
        data = pd.Series(資料列表, index = 索引列表)
        print(data[索引])
        ```
- 統計相關
  - `data.sum()`、`data.max()`、`data.prod()`、`data.mean()`、`data.median()`、`data.std()`、`data.nlargest(3)` 最大的三項、`data.nsmallest(2)` 最小的兩項
- 字串運算
    ```python
    import pandas as pd
    data - pd.Series(["您好", "Python", "Pandas"])
    data.str.len()
    data.str.cat(sep = ",")
    data.str.contains("P")
    data.str.replace("您好", "Hello")
    ```

### Pandas 資料分析 - DataFrame
- 雙維度
- 建立 DataFrame
    ```python
    pd.DataFrame(字典)
    ```


