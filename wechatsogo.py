import wechatsogou

#https://github.com/Chyroc/WechatSogou
ws_api =wechatsogou.WechatSogouAPI()

#获取特定公众号信息 - get_gzh_info
data1=ws_api.get_gzh_info('别妞')

#搜索公众号
data2=ws_api.search_gzh('别妞')

#搜索微信文章
data3=ws_api.search_article('别妞')

print(data1)
print(data2)
print(data3)
