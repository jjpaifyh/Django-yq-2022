from django.shortcuts import render, redirect
from pymysql import Connect
from .sqlData import *


def getData(request):
    gauge_data = gaugeData()
    data_x, data_y = lineData()
    scatter_data = scatterData()
    data_geoLine_lines, data_geoLine_scatter = geoLinesData()
    data_map = mapData()
    pie_data = pieData()
    river_data = themeRiverData()
    key, value = wordCloudData()
    print(pie_data)
    return render(request, "mainBox.html", {"data_x": data_x, "data_y": data_y,
                                            "scatter_data": scatter_data,
                                            "gauge_data": gauge_data,
                                            "data_geoLine_lines": data_geoLine_lines,
                                            "data_geoLine_scatter": data_geoLine_scatter,
                                            "data_map": data_map,
                                            "pie_data": pie_data,
                                            "river_data": river_data,
                                            "key": key, "value": value})


def to_login(request):
    return render(request, "login.html")


def check_login(request):
    username = request.POST["username"]
    password = request.POST.get("password")
    conn = Connect(user="root",
                   password="123456",
                   host="127.0.0.1",
                   database="visual_db_2018",
                   port=3306,
                   charset="utf8")
    cur = conn.cursor()
    sql = """SELECT * FROM user_info WHERE username = %s AND password = %s"""
    cur.execute(sql, (username, password))
    data = cur.fetchall()
    print(data)
    cur.close()
    conn.close()
    if len(data) > 0:
        return redirect("/req/")
    else:
        return render(request, "login.html", context={"msg": "用户名或密码错误"})