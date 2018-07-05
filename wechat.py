#!/usr/bin/env python
# -*- coding:utf-8 -*-

import itchat
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
import os
import numpy as np
from pyecharts import Map

def login():
    itchat.auto_login(hotReload=True)
    itchat.dump_login_status()

def sendFile():
    itchat.send_file("/Users/zachary/Pictures/vpn.jpg")

def changeDir():
    os.chdir('/Users/zachary/Desktop')  # 更改工作目录为桌面

cities = []
def getFriendsAndSaveAsEcxel():
    friends = itchat.get_friends(update=True)[:]
    print(friends)
    total = len(friends) - 1
    male = female = other = 0
    wb = workbook.Workbook()  # 创建Excel对象
    ws = wb.active  # 获取当前正在操作的表对象
    ws.append(['昵称', '备注', '性别', '省份', '城市', '个性签名'])

    for friend in friends[1:]:
        Sex = friend["Sex"]
        NickName = friend["NickName"]
        Province = friend["Province"]
        City = friend["City"]
        Signature = friend["Signature"]
        RemarkName = friend["RemarkName"]
        #绘制地图用
        cities.append(City+'市')
        if Sex == 1:
            male += 1
            Sex = '男'
        elif Sex == 2:
            Sex = '女'
            female += 1
        else:
            other += 1
            Sex = '不男不女'
        # 往表中写入标题行,以列表形式写入！
        ws.append([NickName, RemarkName, Sex, Province ,City, Signature])
    #wb.save('wechat.xlsx')  # 存入所有信息后，保存为filename.xlsx
    print("男性好友：%.2f%%" % (float(male) / total * 100))
    print("女性好友：%.2f%%" % (float(female) / total * 100))
    print("其他：%.2f%%" % (float(other) / total * 100))

def drawMap():
    city_list = ["厦门市","福州市","泉州市","莆田市","宁德市","漳州市","龙岩市","三明市","南平市"]
    num = []
    for city in city_list:
        num.append(cities.count(city))
    map = Map("我的微信好友分布图",width=1200,height=600)
    print(num)
    print(city_list)
    #map.add("",省市列表,省市占比,maptype{china或省市名字}，is_visualmap=True{是否显示色块}，visual_text_color{标签字体颜色})
    map.add("", city_list, num, maptype='福建', visual_range=[0, 150], visual_text_color='#000')

    #map.show_config()打印json配置数据
    map.render()


login()
# sendFile()
# changeDir()
# getFriendsAndSaveAsEcxel()
# drawMap()
print("保存成功")
