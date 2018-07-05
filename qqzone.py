#coding:utf-8
#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import importlib2
import sys
importlib2.reload(sys)


def startSpider():
    driver = webdriver.Chrome('/Users/zachary/zachary/chromedriver.exe') #这个是chormedriver的地址
    driver.get('https://qzone.qq.com/')

    driver.switch_to.frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()

    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys('337047207')  #这里填写你的QQ号
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('')  #这里填写你的QQ密码


    driver.find_element_by_id('login_button').click()
    time.sleep(2)


    f = open('/Users/zachary/Documents/bobo.txt','w')

    #---------------获得g_qzonetoken 和 gtk
    html = driver.page_source

    '''g_qzonetoken=re.search('window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',html)#从网页源码中提取g_qzonetoken'''
    g_qzonetoken = "e794139a284d6ea9e0b26826e541b55df37d0667a3544f534de25aebdb64628d3ab75e1d7104bbb22a"

    cookie = {}#初始化cookie字典
    for elem in driver.get_cookies():#取cookies
        cookie[elem['name']] = elem['value']

    gtk=getGTK(cookie)#通过getGTK函数计算gtk
    #print(g_qzonetoken)
    #print(gtk)



    #--------------获得好友列表   注意下面的链接
    driver.get('https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_hat_get.cgi?hat_seed=1&uin=337047207&fupdate=1&g_tk='+str(gtk)+'&qzonetoken='+str(g_qzonetoken)+'&g_tk='+str(gtk))
    friend_list = driver.page_source
    friend_list = str( friend_list )
    abtract_pattern  =  re.compile('\"(.\d*)\":\{\\n"realname":"(.*?)"}',re.S)
    QQ_name_list = re.findall(abtract_pattern,str(friend_list)) #数组
    print(QQ_name_list)
    numList=dict()# numList => (QQnum:QQname)  #列表
    for i in QQ_name_list:
        numList[str(i[0])]=str(i[1])
    begin = 0
    last_source = ""
    tag = 1
    first = 0
    firstTime=""

    numList['337047207']='周黎峰'
    #print(numList)



    for key in numList.keys():
        QQnum = key
        QQname = numList[QQnum]

        if QQnum == "337047207":  #查找指定好友说说
            count = 1
            begin = 0
            while tag==1 :
                #-------------进入好友说说页面                                                                       #'+QQnum+'              '+str(begin)+'
                #print("Begin:"+str(begin))
                driver.get('https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin='+QQnum+'&ftype=0&sort=0&pos='+str(begin)+'&num=40&replynum=200&g_tk='+str(gtk)+'&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken='+str(g_qzonetoken)+'&g_tk='+str(gtk))

                try:
                    msg_list_json = driver.page_source
                except:
                    begin = begin + 40
                    continue


                msg_list_json = str(msg_list_json)
                if last_source==msg_list_json :
                    break
                else:
                    last_source=msg_list_json



                #检测是否没有权限访问
                abtract_pattern  =  re.compile(',"message":"(.*?)","name":',re.S)
                message = re.findall(abtract_pattern,str(msg_list_json))
                if message!=[]:
                    if str(message[0])=='对不起,主人设置了保密,您没有权限查看':#对不起,主人设置了保密,您没有权限查看
                        break

                #print(msg_list_json)
                #解析JSON
                #webDriver没有现成的JSON解析器，所以采用获取源码的方式，然后使用正则表达式获取具体细节
                msg_list_json =  msg_list_json.split("msglist")[1]#拆分json，缩小范围，也能加快解析速度
                msg_list_json =  msg_list_json.split("smoothpolicy")[0]
                msg_list_json =  msg_list_json.split("commentlist")[1:]


                #说说动态分4种：1、文字说说（或带有配图的文字说说）
                #              2、只有图片的说说
                #              3、转发，并配有文字
                #              4、转发，不配文字

                for text in msg_list_json:
                    # 1、先检查说说，用户是否发送了文字，如果没有文字，正则表达式匹配无效
                    abtract_pattern  =  re.compile('\}\],"content":"(.*?)","createTime":"(.*?)","created_time":(.*?),"',re.S)
                    msg_time = re.findall(abtract_pattern,str(text))

                    if msg_time!=[]:
                        # 2、如果作者说说有文字，那么检查是否有转发内容
                        msg = str(msg_time[0][0])
                        sendTime = str(msg_time[0][1])

                        abtract_pattern  = re.compile('\}\],"content":"(.*?)"},"rt_createTime":"(.*?)","',re.S)
                        text = text.split("created_time")[1]
                        msg_time2 = re.findall(abtract_pattern,str(text))

                        #合并发送内容 格式：评论+转发内容
                        if msg_time2!=[]:
                            msg = msg +"  转发内容:"+str(msg_time2[0][0])

                    else:
                        # 3、说说内容为空，检查是否为 =>只有图片的说说 or 转发，不配文字
                        #获取正文发送时间 （发送时间分为：正文发送时间 or 转发时间）
                        abtract_pattern  =  re.compile('"conlist":null,"content":"","createTime":"(.*?)",',re.S)
                        msgNull_time = re.findall(abtract_pattern,str(text))

                        if msgNull_time!=[]:
                            #如果有正文发送时间，那么就是这条说说仅含有图片  =>只有图片的说说
                            msg = "图片"
                            sendTime = str(msgNull_time[0])
                        else:
                            #如果没有正文发送时间，那么就是说这条说为 =>转发，不配文字
                            abtract_pattern  =  re.compile('\}\],"content":"(.*?)"},"rt_createTime":"(.*?)","',re.S)
                            msg_time = re.findall(abtract_pattern,str(text))
                            msg ="  转发内容:"+str(msg_time[0][0])
                            sendTime = str(msg_time[0][1])

                    #写入本地文件
                    #f.write('{},{},{},{}\n'.format(str(QQname),str(QQnum),sendTime,msg))


                    print(str(count)+" : "+str(QQname)+" : "+str(QQnum)+" : "+sendTime+" : "+msg)
                    count = count + 1

                begin =  begin + 40



def getGTK(cookie):
    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)
    return hashes & 0x7fffffff
startSpider()
print("爬取结束")