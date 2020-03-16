def create_sql(values):

    sql_template = '''
    select DATE_FORMAT(create_time,'%H') as hours,count(1) as thisCount 
from action_log t where t.data_type='{data_type}' and t.action='{action}' 
and t.create_time>'{create_time_start}' and t.create_time<'{create_time_end}' 
and t.description in ({ips}) 
group by hours
    '''
    sql = sql_template.format(**values)
    return sql
