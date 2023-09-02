from apps.app import db
from apps.auth.forms import SignUpForm, LoginForm
from apps.crud.models import User
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user
from flask import Flask, render_template_string, Response, jsonify
from apps.crud.models import Price
import csv
import pandas as pd
import datetime
from datetime import date, timedelta
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
from apps.home.csv_test import pricelist

# 使用Blueprint產生home
home = Blueprint("home", __name__, template_folder="templates", static_folder="static")

qkname = [
    '桂格大燕麥片即沖即食歷史價格',
    '桂格大燕麥片嚴選薄片歷史價格',
    '桂格原片原味大燕麥片歷史價格',
    '桂格紅麴蕎麥大燕麥片歷史價格',
    '桂格紫米山藥大燕麥片歷史價格',
    '桂格有機大燕麥片歷史價格',
    '桂格機能燕麥片歷史價格',
    '桂格高鈣燕麥片歷史價格'
]
@home.before_request
def before_request():
    # 這個函數會在每次請求之前執行
    pass

# 建立index端點
@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/index1")
#@login_required
def index1():
    for i in range(1, 9):
        qkread(i, qkname[i-1])

    return render_template("home/index1.html")

def qkread(num, name):
    # 讀取CSV檔案
    csv_outfolder = os.path.join(os.path.dirname(__file__), 'csvoutput')
    csvname = 'result' + str(num) + '.csv'
    csv_path = os.path.join(csv_outfolder, csvname)
    data = pd.read_csv(csv_path)
    # 將日期欄位轉換為日期型別
    data['日期'] = pd.to_datetime(data['日期'])

    # 取得中文字型的路徑
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'msjhbd.ttc')
    # 設定中文字型
    font = FontProperties(fname=font_path)
    # 創建新的虛擬圖形
    plt.figure()
    # 繪製條狀圖
    plt.bar(data['日期'], data['每100g價格'])
    plt.xlabel('日期', fontproperties=font)
    plt.ylabel('每100g價格', fontproperties=font)
    plt.title(name, fontproperties=font)
    plt.xticks(rotation=45)
    # 設定字型
    fontset = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 6}
    # 在每個條狀上標示價格數值
    for i, value in enumerate(data['每100g價格']):
        if (i%2)!=0:
            plt.text(data['日期'][i], value + 0.2, str(value), ha='center', fontdict=fontset)  # 調整位置和偏移量
    
    # 設定Y軸範圍
    plt.ylim(0, max(data['每100g價格']) + 6)
    pngname = 'qk' + str(num) + '_output.png'
    png_path = os.path.join(os.path.dirname(__file__), 'static', 'dist', 'png', pngname)
    plt.savefig(png_path, format='png', bbox_inches='tight')
    # 關閉虛擬圖形
    plt.close()
    

@home.route("/index2")
#@login_required
def index2():
    # 讀取CSV檔案
    csv_outfolder = os.path.join(os.path.dirname(__file__), 'csvoutput')
    csv_path = os.path.join(csv_outfolder, 'result10.csv')
    data = pd.read_csv(csv_path)
    # 將日期欄位轉換為日期型別
    data['日期'] = pd.to_datetime(data['日期'])

    # 取得中文字型的路徑
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'msjhbd.ttc')
    # 設定中文字型
    font = FontProperties(fname=font_path)
    # 創建新的虛擬圖形
    plt.figure()
    # 繪製條狀圖
    plt.bar(data['日期'], data['每100g價格'])
    plt.xlabel('日期', fontproperties=font)
    plt.ylabel('每100g價格', fontproperties=font)
    plt.title('台糖燕麥歷史價格', fontproperties=font)
    plt.xticks(rotation=45)
    # 設定字型
    fontset = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 6}
    # 在每個條狀上標示價格數值
    for i, value in enumerate(data['每100g價格']):
        if (i%2)!=0:
            plt.text(data['日期'][i], value + 0.2, str(value), ha='center', fontdict=fontset)  # 調整位置和偏移量
    
    # 設定Y軸範圍
    plt.ylim(0, max(data['每100g價格']) + 2)
    png_path = os.path.join(os.path.dirname(__file__), 'static', 'dist', 'png', 'tsc_output.png')
    plt.savefig(png_path, format='png', bbox_inches='tight')
    # 關閉虛擬圖形
    plt.close()
    return render_template("home/index2.html")

@home.route("/index3")
#@login_required
def index3():
    csv_outfolder = os.path.join(os.path.dirname(__file__), 'csvoutput')
    csv_path = os.path.join(csv_outfolder, 'result9.csv')
    data = pd.read_csv(csv_path)
    # 將日期欄位轉換為日期型別
    data['日期'] = pd.to_datetime(data['日期'])

    # 取得中文字型的路徑
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'msjhbd.ttc')
    # 設定中文字型
    font = FontProperties(fname=font_path)
    # 創建新的虛擬圖形
    plt.figure()
    # 繪製條狀圖
    plt.bar(data['日期'], data['每100g價格'])
    plt.xlabel('日期', fontproperties=font)
    plt.ylabel('每100g價格', fontproperties=font)
    plt.title('馬玉山高纖大燕麥片歷史價格', fontproperties=font)
    plt.xticks(rotation=45)
    # 設定字型
    fontset = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 6}
    # 在每個條狀上標示價格數值
    for i, value in enumerate(data['每100g價格']):
        if (i%2)!=0:
            plt.text(data['日期'][i], value + 0.2, str(value), ha='center', fontdict=fontset)  # 調整位置和偏移量
    
    # 設定Y軸範圍
    plt.ylim(0, max(data['每100g價格']) + 3)
    png_path = os.path.join(os.path.dirname(__file__), 'static', 'dist', 'png', 'mus_output.png')
    plt.savefig(png_path, format='png', bbox_inches='tight')
    # 關閉虛擬圖形
    plt.close()
    return render_template("home/index3.html")

@home.route("/process_prediction", methods=['POST'])
def process_prediction():
    print("======process prediction======")
    data = request.get_json()
    prediction = data.get('prediction')

    if prediction == "QKFN":
        response_message = "this is QKFN"
    elif prediction == "QKHC":
        response_message = "this is QKHC"
    elif prediction == "QKYM":
        response_message = "this is QKYM"
    else:
        response_message = "this is Oats"

    return jsonify({"message": response_message})
