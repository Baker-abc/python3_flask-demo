def create_render_sql(values):
    sql_template = '''
select t.task_status, count(1) from job_task_info t where t.task_type=1  and t.update_time>'{create_time_start}' 
and t.update_time<'{create_time_end}' 
and t.task_result_info like '%{render_type}%'
group by t.task_status
    '''
    sql = sql_template.format(**values)
    return sql


def create_3d_pak_mdesk_sql(values):
    sql_template = '''
select t.task_status ,count(1) from job_task_info t where t.task_type='{task_type}' and t.update_time>'{create_time_start}' 
and t.update_time<'{create_time_end}' 
group by t.task_status
    '''
    sql = sql_template.format(**values)
    return sql

def create_gallery_sql(values):
    sql_template = '''
    SELECT count(1) as total FROM design_gallery where update_time>'{create_time_start}' and update_time<'{create_time_end}' 
    '''
    sql = sql_template.format(**values)
    return sql

def create_design_sql(values):
    sql_template = '''
    SELECT count(1) FROM design where update_time>'{create_time_start}' and update_time<'{create_time_end}' 
    '''
    sql = sql_template.format(**values)
    return sql
