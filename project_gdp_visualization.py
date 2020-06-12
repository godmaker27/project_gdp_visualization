#coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：19级植物生产类3班郑凯伦
日期：2020/6/8
"""

import csv
import math
import pygal
import pygal.maps.world  


def read_csv_as_nested_dict(filename, keyfield): 
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row

    return result
    
gdp_countries=read_csv_as_nested_dict("isp_gdp.csv","Country Name")
pygal_countries = pygal.maps.world.COUNTRIES
print(pygal_countries)

def reconcile_countries_by_name(plot_countries, gdp_countries):
   
    dict0={}
    set0=set()
    for i in plot_countries:
        country_name=plot_countries[i] 
        result = country_name in gdp_countries
        if result==True:
            dict0[i]=country_name
        if result==False:
            set0.add(i)
    tuple0=(dict0,set0)
    print(tuple0)
    return tuple0








def build_map_dict_by_name(gdpinfo, plot_countries, year):
    tuple0=reconcile_countries_by_name(plot_countries, gdp_countries)
    dict1=tuple0[0]
    set0=tuple0[1]
    set1=set()
    dict2={}
    for i in dict1:
	    countryname=dict1[i]
	    dictt=gdp_countries[countryname]
	    value0=dictt[year]
	    if value0=="":
		    set1.add(i)
	    else:
		    value0=float(value0)
		    value0=math.log10(value0)
		    dict2[i]=value0
    tuple1=(dict2,set0,set1)
    print(tuple1)
    return(tuple1)

def render_world_map(gdpinfo, plot_countries, year, map_file): 
    tuple1=build_map_dict_by_name(gdpinfo, plot_countries, year)
    dict2=tuple1[0]
    set0=tuple1[1]
    set1=tuple1[2]
    gdp_world_map=pygal.maps.world.World()
    gdp_world_map.title="全球GDP分布图"
    gdp_world_map.add(year,dict2)
    gdp_world_map.add("missing from world bank",set0)
    gdp_world_map.add("no data at this year",set1)
    gdp_world_map.render_to_file(map_file)

def test_render_world_map(year):  
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }
    

    pygal_countries = pygal.maps.world.COUNTRIES   
    
    
    render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_Years.svg")

    

    




#程序测试和运行
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year=input("请输入需查询的具体年份:")
test_render_world_map(year)
