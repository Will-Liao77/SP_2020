# System Programming 1091 Final hw

```diff
- 欲執行PLY請輸入：python mylex.py 
```

# 語法：
## 冪次運算： num '^' num
```diff
calc > 2^3 
```

```diff
根號運算：num '**' num
e.g. calc > 4**2 
```

```diff
for-loop：for 起始值 to 結束 ("欲執行的指令運算")
e.g.
``` 
![image](https://github.com/huikaiwang/SP_2020/blob/main/img/截圖%202020-12-19%20下午5.39.00.png?raw=true)

```diff
if-else運算：if ("條件判斷") "expression" else "expression" 
e.g.
``` 
![image](https://github.com/huikaiwang/SP_2020/blob/main/img/截圖%202020-12-19%20下午5.40.33.png?raw=true)

```diff
若輸入四則運算，則會把Three-Address Code一一列出
如下
``` 
![image](https://github.com/huikaiwang/SP_2020/blob/main/img/截圖%202020-12-20%20下午4.40.37.png)

```diff
最後在原.py檔的資料夾內會多一份.png檔，為依據上述所建立的一棵Parsing Tree
如下
``` 
![image](https://github.com/huikaiwang/SP_2020/blob/main/img/nx_test.png)
