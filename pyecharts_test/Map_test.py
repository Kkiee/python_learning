import json
from pyecharts.charts import Map
from pyecharts.options import *

f=open("D:/疫情.txt","r",encoding="UTF-8")
data=f.read()
f.close()
data_dict=json.loads(data)
province_data_list=data_dict["areaTree"][0]["children"]
data_list=[]
for province_data in province_data_list:
    province_name=province_data["name"]
    province_confirm=province_data["total"]["confirm"]
    data_list.append((province_name,province_confirm))
map=Map()
map.add("各省份确认人数",data_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[{"min": 1,"max":99,"Lable":"1~99人","coLor":"#CCFFFA"},
                {"min": 100,"max":999,"Lable":"100~9999人","color":"#FFFF99"},
                {"min":1000,"max":4999,"Lable":"1000~4999人","color":"#FF9966"},
                {"min":5000,"max":9999,"Lable":"5000~99999人","color":"#FF6666"},
                {"min": 10000,"max":99999,"Lable":"10000~99999人","color":"#CC3333"},
                {"min": 100000,"max":99999,"lable":"100000~999999","color":"#990033"},
        ]
    )
)
map.render("全国疫情地图.html")