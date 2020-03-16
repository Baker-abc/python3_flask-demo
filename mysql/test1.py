import mysql.connector
import sql_template
import logging


def exex(service_name, create_time_start, create_time_end, start_progress, end_progress, filter_progress1,
         filter_progress2):
    mydb = mysql.connector.connect(
        host="",  # 数据库主机地址
        user="",  # 数据库用户名
        passwd="",  # 数据库密码
        database=""
    )


    mycursor = mydb.cursor()

    values = {
        'create_time_start': create_time_start,
        'create_time_end': create_time_end,
        'service_name': service_name,
        'start_progress': start_progress,
        'end_progress': end_progress,
        'filter_progress1': filter_progress1,
        'filter_progress2': filter_progress2
    }

    sql = sql_template.create_sql(values)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        logging.info("{0} --- {1}：【总计{2}】 【耗时{3}】".format(start_progress, end_progress, x[0], x[1]))


if __name__ == '__main__':
    logging.basicConfig(
        handlers=[logging.FileHandler("info.log", encoding="utf-8"), logging.StreamHandler()],
        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
        datefmt="%Y-%M-%d %H:%M:%S", level=logging.DEBUG)

    create_time_start = '2020-01-07 00:00:00'
    create_time_end = '2020-01-07 23:59:59'

    logging.info("-------转换-------")
    exex("rendering-package-worker", create_time_start, create_time_end, 'pull_job', 'download_data', '', '')
    exex("rendering-package-worker", create_time_start, create_time_end, 'download_data', 'node_execute', '', '')
    exex("rendering-package-worker", create_time_start, create_time_end, 'node_execute', 'upload_oss', '', '')
    exex("rendering-package-worker", create_time_start, create_time_end, 'upload_oss', 'success', '', '')
    exex("rendering-package-worker", create_time_start, create_time_end, 'success', 'delete_local_files', '', '')

    logging.info("---------打包----------")
    exex("render", create_time_start, create_time_end, 'pull_job', 'download_data', '', '')
    exex("render", create_time_start, create_time_end, 'download_data', 'node_execute', '', '')
    exex("render", create_time_start, create_time_end, 'node_execute', 'copy_to_dir', '', '')
    exex("render", create_time_start, create_time_end, 'copy_to_dir', 'success', '', '')
    exex("render", create_time_start, create_time_end, 'success', 'delete_local_files', '', '')

    logging.info("---------渲染---------")
    exex("render", create_time_start, create_time_end, 'delete_local_files', 'render_pull', '', '')
    exex("render", create_time_start, create_time_end, 'render_pull', 'render_start', '', '')
    exex("render", create_time_start, create_time_end, 'render_start', 'render_success', '', '')
    exex("render", create_time_start, create_time_end, 'render_success', 'update_jobmanager_success',
         'createlabel_success', 'analysis_label_success')
    logging.info("---------渲染（获取商品标签）---------")
    exex("render", create_time_start, create_time_end, 'render_success', 'createlabel_success', '', '')
    exex("render", create_time_start, create_time_end, 'createlabel_success', 'analysis_label_success', '', '')
    exex("render", create_time_start, create_time_end, 'analysis_label_success', 'update_jobmanager_success', '', '')
