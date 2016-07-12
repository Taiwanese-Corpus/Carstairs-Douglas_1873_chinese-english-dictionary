# 廈英大辭典
杜嘉德(Douglas, Carstairs)在1873年編的廈英大辭典(Chinese-English Dictionary of the Vernacular or Spoken Language of Amoy)  

原始掃描檔詳見[台語文記憶](http://ip194097.ntcu.edu.tw/memory/tgb/thak.asp?id=115&page=1)

## 資料夾介紹
### 原始資料
二次校對的資料，是`doc`格式

### xls資料
只有音標開頭是`A`和`B`的資料！！
2005-04-12寄出的資料，是xls格式。

### csv格式資料
用程式對`原始資料`整理過來的`csv`
```
sudo apt-get install -y wv g++ libxml2-dev libxslt1-dev python3-dev
virtualenv --python python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install beautifulsoup4 lxml
python 轉換doc.py
```