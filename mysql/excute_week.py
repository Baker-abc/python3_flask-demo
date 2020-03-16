import mysql.connector
import sql_template_week
import logging


def exex_render(task_type, render_type, create_time_start, create_time_end, database):

    mydb = None
    if database == "":
        mydb = mysql.connector.connect(
            host="",  # 数据库主机地址
            user="",  # 数据库用户名
            passwd="",  # 数据库密码
            database=""
        )
    else:
        mydb = mysql.connector.connect(
            host="",  # 数据库主机地址
            user="",  # 数据库用户名
            passwd="",  # 数据库密码
            database=""
        )

    mycursor = mydb.cursor()

    sql = ""
    if task_type == 1:
        values = {
            'render_type': render_type,
            'create_time_start': create_time_start,
            'create_time_end': create_time_end
        }
        sql = sql_template_week.create_render_sql(values)
    else:
        values = {
            'task_type': task_type,
            'create_time_start': create_time_start,
            'create_time_end': create_time_end
        }
        sql = sql_template_week.create_3d_pak_mdesk_sql(values)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    total = 0
    success = 0
    for x in myresult:
        total = total + x[1]
        if x[0] == 1:
            success = x[1]

    rate = "100%"
    if total != 0:
        rate = str(round(success / total * 100, 4)) + "%"

    print(
        "{0} ---- {1} ------- {2} ---- {3}".format(task_type, render_type, total, rate))


def gallery_design(task_type, create_time_start, create_time_end, database):

    mydb = None
    mydb = mysql.connector.connect(
        host="",  # 数据库主机地址
        user="",  # 数据库用户名
        passwd="",  # 数据库密码
        database=""
    )

    mycursor = mydb.cursor()

    sql = ""
    if task_type == "gallery":
        values = {
            'create_time_start': create_time_start,
            'create_time_end': create_time_end
        }
        sql = sql_template_week.create_gallery_sql(values)
    else:
        values = {
            'create_time_start': create_time_start,
            'create_time_end': create_time_end
        }
        sql = sql_template_week.create_design_sql(values)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print("{0} ------- {1}".format(task_type, x[0]))


if __name__ == '__main__':
    logging.basicConfig(
        handlers=[logging.FileHandler(
            "info.log", encoding="utf-8"), logging.StreamHandler()],
        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
        datefmt="%Y-%M-%d %H:%M:%S", level=logging.DEBUG)

    create_time_start = '2020-03-07 00:00:00'
    create_time_end = '2020-03-13 23:59:59'

    print("====================== alpha 渲染 =================")
    exex_render(1, '"RenderType":"ordinary"', create_time_start,
                create_time_end, 'jobs-alpha')
    exex_render(1, '"RenderType":"panorama"', create_time_start,
                create_time_end, 'jobs-alpha')
    exex_render(1, '"RenderType":"image"', create_time_start,
                create_time_end, 'jobs-alpha')
    exex_render(1, '"RenderType":"cabinet"', create_time_start,
                create_time_end, 'jobs-alpha')
    exex_render(1, '"RenderType":"uehouseplan"',
                create_time_start, create_time_end, 'jobs-alpha')
    exex_render(1, '"RenderType":"task_model_render"',
                create_time_start, create_time_end, 'jobs-alpha')

    print("====================== beta 渲染 =================")
    exex_render(1, '"RenderType":"ordinary"',
                create_time_start, create_time_end, 'jobs')
    exex_render(1, '"RenderType":"panorama"',
                create_time_start, create_time_end, 'jobs')
    exex_render(1, '"RenderType":"image"',
                create_time_start, create_time_end, 'jobs')
    exex_render(1, '"RenderType":"cabinet"',
                create_time_start, create_time_end, 'jobs')
    exex_render(1, '"RenderType":"uehouseplan"',
                create_time_start, create_time_end, 'jobs')
    exex_render(1, '"RenderType":"task_model_render"',
                create_time_start, create_time_end, 'jobs')

    print("====================== alpha  =================")
    exex_render(6, '硬装', create_time_start, create_time_end, 'jobs-alpha')
    exex_render(3, '模型3d', create_time_start, create_time_end, 'jobs-alpha')
    exex_render(25, 'AI跑材质图', create_time_start, create_time_end, 'jobs-alpha')

    print("====================== beta  =================")
    exex_render(6, '硬装', create_time_start, create_time_end, 'jobs')
    exex_render(3, '模型3d', create_time_start, create_time_end, 'jobs')
    exex_render(22, 'pak', create_time_start, create_time_end, 'jobs')

    print("====================== alpha  大数据  =================")
    gallery_design("gallery",  create_time_start, create_time_end, 'design')
    gallery_design("design",  create_time_start, create_time_end, 'design')
