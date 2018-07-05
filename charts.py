from pyecharts import Bar

def drawZhuZhuangTu_x():
    bar =Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    bar.show_config()
    bar.render()

def drawEffectScatter():
    from pyecharts import EffectScatter
    # v1 = [10, 20, 30, 40, 50, 60]
    # v2 = [25, 20, 15, 10, 60, 33]
    # es = EffectScatter("动态散点图示例")
    # es.add("effectScatter", v1, v2)
    # es.render()

    es = EffectScatter("动态散点图各种图形示例")
    es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
    es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4, symbol="rect")
    es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5, symbol="roundRect")
    es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill', symbol="diamond")
    es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3, symbol="arrow")
    es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3, symbol="triangle")
    es.render()

def drawMap():
    from pyecharts import Map
    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
    map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
    map.show_config()
    map.render()


drawZhuZhuangTu_x()
#drawEffectScatter()
drawMap()
