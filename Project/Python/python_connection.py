import pymysql

import psycopg2

def get_connection(conn_info, conn_database=None):
    """
        获取连接
    """
    error_str = '%s 数据库连接失败，请检查连接的数据库是否输入错误'
    conn = None
    try:
        conn_func = psycopg2.connect
        if not conn_info.get('sslmode', None):
            conn_func = pymysql.connect
        conn = conn_func(host=conn_info.get('host'), user=conn_info.get('user'), password=conn_info.get('password'), database=conn_database if conn_database else conn_info.get('database'), port=conn_info.get('port', None))
    except psycopg2.Error:
        print(error_str % 'postgre ')
    except pymysql.Error:
        print(error_str % 'mysql ')
    return conn

def close_conn(conn):
    """
        关闭连接或者游标
    """
    conn.close()

def get_cursor(conn, cursor_type=None):
    """
        获取游标
        '''
            pymysql 游标类型
                Cursor	            普通的游标对象，默认创建的游标对象
                SSCursor	        不缓存游标，主要用于当操作需要返回大量数据的时候
                DictCursor	        以字典的形式返回操作结果
                SSDictCursor	    不缓存游标，将结果以字典的形式进行返回
        '''
        '''
            psycopg2 游标类型
                DictCursorBase
                DictCursor
                RealDictCursor
                NamedTupleCursor
                LoggingCursor
                MinTimeLoggingCursor
                ReplicationCursor
        '''
    """
    cursor = conn.cursor(cursor_type)
    return cursor

# 连接MySQL数据库的配置
mysql_config_information = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'information_schema',
}
# 连接pg数据库的配置
pg_config_information = {
    'host': 'db13-03.dev.mypscloud.com',
    'user': 'odoo',
    'password': 'IJW8C3vhS4XbKNJh',
    'database': 'postgres',
    'port': 35434,
    'sslmode': 'prefer',
}

def get_database_list(conn):
    '''
        获取所有的数据
    '''
    db_sql = "select datname from pg_database where not datistemplate and datallowconn and datname not in ('postgres')"
    if not hasattr(conn, 'dsn'):
        db_sql = "show databases"
    db_list = []
    cursor = conn.cursor()
    cursor.execute(db_sql)
    db_list_result = cursor.fetchall()
    for database in db_list_result:
        print(database[0])
    close_conn(cursor)

def execute(cursor, sql):
    """
        执行SQL语句
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    print('结果为: ')
    for x in result:
        print(x)



if __name__ == '__main__':
    # 选择连接的数据库类型（MySQL或者postgre）
    db_type = input('请选择要连接的数据库种类：MySQL | postgre\n').lower()
    conn_info = None
    if db_type and db_type == 'mysql':
        conn_info = mysql_config_information
    elif db_type and db_type in ['pg', 'postgre', 'postgres']:
        conn_info = pg_config_information

    # 获取连接
    conn = get_connection(conn_info)
    print('存在以下数据库: ')
    get_database_list(conn)
    database = input('请选择要连接的数据库')
    close_conn(conn)
    conn = get_connection(conn_info, conn_database=database)
    cr = get_cursor(conn)

    # 获取游标
    while True:
        sql_str = input('请输入SQL语句：').lower()
        if not sql_str or sql_str == 'exit':
            break
        execute(cr, sql=sql_str)
        # 进行数据库操作
    # 关闭游标与连接
    close_conn(cr)
    close_conn(conn)