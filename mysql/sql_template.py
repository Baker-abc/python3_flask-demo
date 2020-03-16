def create_sql(values):

    sql_template = '''
    SELECT
	a.count,
	(a.sum - b.sum) / a.count AS 'cost'
FROM
	(
		(
			SELECT
				t2.service_name,
				sum(
					UNIX_TIMESTAMP(t2.create_time)
				) AS sum,
				count(1) AS count
			FROM
				action_log t2
			WHERE
				t2.id IN (
					SELECT
						id
					FROM
						(
							SELECT
								MAX(id) AS id
							FROM
								action_log
							WHERE
								service_name = '{service_name}'
							AND create_time > '{create_time_start}'
							AND create_time < '{create_time_end}'
							AND biz_id IN (
								SELECT
									biz_id
								FROM
									(
										SELECT
											biz_id
										FROM
											action_log
										WHERE
											service_name = '{service_name}'
										AND description = '{end_progress}'
										AND create_time > '{create_time_start}'
										AND create_time < '{create_time_end}' 
										AND biz_id IN (
											SELECT
												biz_id
											FROM
												(
													SELECT
														biz_id
													FROM
														action_log
													WHERE
														service_name = '{service_name}'
													AND description = '{start_progress}'
													AND create_time > '{create_time_start}'
													AND create_time < '{create_time_end}' 
													AND biz_id NOT IN (
														SELECT
															biz_id
														FROM
															(
																SELECT
																	biz_id
																FROM
																	action_log
																WHERE
																	service_name = '{service_name}'
																AND (description = '{filter_progress1}' or description = '{filter_progress2}')
																AND create_time > '{create_time_start}'
																AND create_time < '{create_time_end}'
															) include2
													)
												) include1
										)
									) suc1
							)
							GROUP BY
								biz_id,
								description
						) b2
				) 
			AND t2.description = '{end_progress}'
			AND t2.service_name = '{service_name}'
			AND t2.create_time > '{create_time_start}'
			AND t2.create_time < '{create_time_end}'
		) AS a         
		JOIN (
			
			SELECT
				t2.service_name,
				sum(
					UNIX_TIMESTAMP(t2.create_time)
				) AS sum,
				count(1) AS count
			FROM
				action_log t2
			WHERE
				t2.id IN (
					SELECT
						id
					FROM
						(
							SELECT
								MAX(id) AS id
							FROM
								action_log
							WHERE
								service_name = '{service_name}'
							AND create_time > '{create_time_start}'
							AND create_time < '{create_time_end}'
							AND biz_id IN (
								SELECT
									biz_id
								FROM
									(
										SELECT
											biz_id
										FROM
											action_log
										WHERE
											service_name = '{service_name}'
										AND description = '{end_progress}'
										AND create_time > '{create_time_start}'
										AND create_time < '{create_time_end}' 
										AND biz_id NOT IN (
											SELECT
												biz_id
											FROM
												(
													SELECT
														biz_id
													FROM
														action_log
													WHERE
														service_name = '{service_name}'
													AND (description = '{filter_progress1}' or description = '{filter_progress2}')
													AND create_time > '{create_time_start}'
													AND create_time < '{create_time_end}'
												) include3
										)
									) suc2
							)
							GROUP BY
								biz_id,
								description
						) b2
				) 
			AND t2.description = '{start_progress}'
			AND t2.service_name = '{service_name}'
			AND t2.create_time > '{create_time_start}'
			AND t2.create_time < '{create_time_end}'
		) AS b ON a.service_name = b.service_name 
	)
    '''
    sql = sql_template.format(**values)
    return sql
