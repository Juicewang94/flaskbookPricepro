import csv
import pandas as pd
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

# 欲辨識商品最便宜包裝，在爬蟲csv檔案中欄位號碼
rownum = [7, 8, 10, 12, 13, 14, 15, 16, 19, 31]
result1 = []
result2 = []
result3 = []
result4 = []
result5 = []
result6 = []
result7 = []
result8 = []
result9 = []
result10 = []

def readcsv(file):
    rows = csv.reader(file)
    j = 0
    for row in rows:
        # 在最便宜包裝欄位號碼中，抓取日期及計算該商品最便宜價格
        if j in rownum:
            #讀取csv file第1欄資料中前4位字串
            #print(row[0][0:4],"--", row[3],"--", row[4],"--", row[5],"--", row[6],"--", row[7])
            lowerprice = 9999
            # 從爬蟲表中取出該商品4家賣場售價
            for index in range(4, 8):
                # 如該賣場無售價則跳過
                if row[index] == "None" or row[index] == "lost":
                    continue
                # 將csv表中賣場售價由str轉成int(因舊csv中售價有小數點，所以統一先轉float再轉int)
                tmp = int(float(row[index]))
                # 找出該商品4家最低價
                if tmp < lowerprice:
                    lowerprice = tmp
            # 如4家賣場都無售價則設為0
            if lowerprice == 9999:
                lowerprice = 0
            # 計算該商品每100克價格，取至小數點後2位
            tmp = "{:.2f}".format((lowerprice/int(row[3]))*100)
            #print(row[0][0:4],"--", tmp)
            if j==7:
                result1.append([row[0][0:4],row[1],tmp])
            elif j==8:
                result2.append([row[0][0:4],row[1],tmp])
            elif j==10:
                result3.append([row[0][0:4],row[1],tmp])
            elif j==12:
                result4.append([row[0][0:4],row[1],tmp])
            elif j==13:
                result5.append([row[0][0:4],row[1],tmp])
            elif j==14:
                result6.append([row[0][0:4],row[1],tmp])
            elif j==15:
                result7.append([row[0][0:4],row[1],tmp])
            elif j==16:
                result8.append([row[0][0:4],row[1],tmp])
            elif j==19:
                result9.append([row[0][0:4],row[1],tmp])
            elif j==31:
                result10.append([row[0][0:4],row[1],tmp])
        j += 1

class pricelist():
    # Start
    date1 = datetime.datetime(date.today().year, date.today().month, date.today().day)
    # 爬蟲儲存csv第一天
    date2 = datetime.datetime(2023, 7, 31)
    # 計算有幾天份的csv需要讀取
    diff = date1 - date2
    d = diff.days + 1
    # 以迴圈分次讀取所有csv檔案(日期順序由舊到新)

    for i in range(d-1, -1, -1):
        filenotfound = 0
        day_interval = timedelta(days=i)
        day_check = date.today() - day_interval
        # 生成檔名與爬蟲csv檔名一致
        filename1 = "scraper_data_" + str(day_check).replace("-", "_") + '_good.csv'
        filename2 = "scraper_data_" + str(day_check).replace("-", "_") + '_bad.csv'
        # 先嘗試開啟good csv檔
        try:
            csv_path = os.path.join(os.path.dirname(__file__), 'csvinput', filename1)
            with open(csv_path, newline='', encoding="utf8") as csvfile:
                readcsv(csvfile)
        except FileNotFoundError:
             filenotfound += 1
             print("file1:" + filename1 + " not found")

        # 若無good csv檔，則嘗試開啟bad csv
        if filenotfound > 0:
            try:
                csv_path = os.path.join(os.path.dirname(__file__), 'csvinput', filename2)
                with open(csv_path, newline='', encoding="utf8") as csvfile:
                    readcsv(csvfile)
            except FileNotFoundError:
                print("file2:" + filename2 + " not found")

#    for i in range(1, 11):
#        outfilename = 'result'+ i + '.csv'

    csv_outfolder = os.path.join(os.path.dirname(__file__), 'csvoutput')
    csv_path = os.path.join(csv_outfolder, 'result1.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result1:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result2.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result2:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result3.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result3:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result4.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result4:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result5.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result5:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result6.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result6:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result7.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result7:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result8.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result8:
        writer.writerow(r)

    csv_path = os.path.join(csv_outfolder, 'result9.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result9:
        writer.writerow(r)
    
    csv_path = os.path.join(csv_outfolder, 'result10.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['編號','日期','每100g價格'])
      for r in result10:
        writer.writerow(r)
#
#    # 讀取CSV檔案
#    csv_path = os.path.join(csv_outfolder, 'result10.csv')
#    data = pd.read_csv(csv_path)
#    # 將日期欄位轉換為日期型別
#    data['日期'] = pd.to_datetime(data['日期'])
#    
#    # 取得中文字型的路徑
#    font_path = os.path.join(os.path.dirname(__file__), 'font', 'msjhbd.ttc')
#    # 設定中文字型
#    font = FontProperties(fname=font_path)
#    # 繪製條狀圖
#    plt.bar(data['日期'], data['每100g價格'])
#    plt.xlabel('日期', fontproperties=font)
#    plt.ylabel('每100g價格', fontproperties=font)
#    plt.title('價格列表', fontproperties=font)
#    plt.xticks(rotation=45)
#    # 在每個條狀上標示價格數值
#    for i, value in enumerate(data['每100g價格']):
#        plt.text(data['日期'][i], value + 0.2, str(value), ha='center', fontproperties=font)  # 調整位置和偏移量
#    
#    # 設定Y軸範圍
#    plt.ylim(0, max(data['每100g價格']) + 2)
#    plt.tight_layout()
#    # 顯示圖表
##    plt.show()

#with open(filename, newline='') as csvfile:
#    rows = csv.reader(csvfile)
#    i = 0
#    for row in rows:
#        if i > 0:
#            #讀取csv file第3欄資料中前4位字串
#            print(row[2][0:4])
#        i += 1

if __name__=='__main__':
	pricelist()