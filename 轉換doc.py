from os.path import join
from posix import listdir
from subprocess import Popen, PIPE

from bs4 import BeautifulSoup
from os import makedirs
from csv import writer


class 轉換doc:

    def __init__(self, 檔名):
        self.檔名 = 檔名

    def 提html(self):
        return self.html

    def 提array(self):
        return self.array

    def doc轉html(self):
        程序 = Popen(['wvWare', self.檔名], stdin=None, stdout=PIPE, stderr=PIPE)
        輸出資訊, _錯誤輸出資訊 = 程序.communicate()
        self.html = 輸出資訊.decode('utf-8', errors="replace")
        return self

    def html轉array(self):
        bs = BeautifulSoup(self.html, "lxml")
        全部資料 = []
        for table in bs.find_all('table'):
            for tr in table.find_all('tr'):
                一逝資料 = []
                for td in tr.find_all('td'):
                    一逝資料.append(td.get_text("", strip=True))
                if len(一逝資料) != 5:
                    print(一逝資料, '格式無仝款！！')
                else:
                    全部資料.append(一逝資料)
        self.array = 全部資料
        return self


def 轉規个資料夾(來源):
    for 檔名 in sorted(listdir(來源), key=lambda 檔名: 檔名[2:]):
        來源檔案 = join(來源, 檔名)
        if 檔名.endswith('doc'):
            print(檔名)
            try:
                for 一逝 in 轉換doc(
                    來源檔案
                ).doc轉html().html轉array().提array():
                    yield 一逝
            except Exception as 錯誤:
                print(來源檔案, 錯誤)

if __name__ == '__main__':
    csv格式資料 = 'csv格式資料'
    makedirs(csv格式資料, exist_ok=True)
    with open(join(csv格式資料, '廈英大辭典-巴克禮增補.csv'), 'w') as 檔案:
        csv檔案 = writer(檔案)
        csv檔案.writerows(轉規个資料夾('原始資料'))
#         for 一逝 in 轉規个資料夾('原始資料'):
#                 print(一逝)
