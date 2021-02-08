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



