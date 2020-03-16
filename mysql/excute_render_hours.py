import mysql.connector
import sql_template_render_hours
import logging


def exex(data_type, action, create_time_start, create_time_end, ips):
    mydb = mysql.connector.connect(
        host="",  # 数据库主机地址
        user="",  # 数据库用户名
        passwd="",  # 数据库密码
        database=""
    )

    mycursor = mydb.cursor()

    values = {
        'data_type': data_type,
        'action': action,
        'create_time_start': create_time_start,
        'create_time_end': create_time_end,
        'ips': ips
    }

    sql = sql_template_render_hours.create_sql(values)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print("【{0}时】-【数量{1}】".format(x[0], x[1]))


def count(start, end, name):
    create_time_start = '2019-12-01 00:00:00'
    create_time_end = '2019-12-31 23:59:59'

    ips = ""
    while start <= end:
        ips = ips + "'172.20.0." + str(start) + "'"
        if start != end:
            ips = ips + ','
        start += 1

    print("====================== 机柜 {0} =================".format(name))
    exex("render-node-service", "event", create_time_start, create_time_end, ips)


if __name__ == '__main__':
    logging.basicConfig(
        handlers=[logging.FileHandler("info.log", encoding="utf-8"), logging.StreamHandler()],
        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
        datefmt="%Y-%M-%d %H:%M:%S", level=logging.DEBUG)

    count(21, 30, "F14")
    count(31, 40, "F15")
    count(41, 50, "F16")
    count(51, 60, "F17")
    count(61, 70, "F18")
    count(71, 80, "F19")
