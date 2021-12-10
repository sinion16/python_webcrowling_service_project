# TEST.ORACLE.PY

import cx_Oracle
import os


location = "C:\instantclient_21_3"
os.environ["PATH"] = location + ";" + os.environ["PATH"]
cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_3")
conn = cx_Oracle.connect("c##student/student@localhost:1521/xe")


def database(list):
    conn = cx_Oracle.connect("c##student/student@localhost:1521/xe")

    def select_count():
        query = 'select count(*) from covid'
        re = []

        cs = conn.cursor()
        re = cs.execute(query)
        for row in re:
            re = row[0]
        return re

    def to_db():
        sysdate = """
                    SELECT COVID_DATE
                    FROM COVID
                    """
        conn = cx_Oracle.connect('c##student/student@localhost:1521/xe')
        cs = conn.cursor()
        rs = cs.execute(sysdate)
        col1 = []
        for record in rs:
            col1.append(record[0])
            date_now = str(col1[0])
            global realdate
            realdate = date_now[2:4] + '/' + date_now[5:7] + '/' + date_now[8:10]
        return realdate

    seoul_num = list[0][0][0]
    korea_num = list[0][1][0]

    tuple_seoul_num = tuple(seoul_num)
    tuple_korea_num = tuple(korea_num)

    date = str(list[1][0])
    date = date[3:11]
    characters = "."
    date = ''.join(x for x in date if x not in characters)
    date = date[:2] + '/' + date[2:4] + '/' + date[4:]
    tp_date = (date,)
    tuple_result = tuple_seoul_num + tuple_korea_num + tp_date

    query = """INSERT INTO COVID VALUES (TO_CHAR(sysdate, 'YY/MM/DD HH24:MI:SS'),:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"""
    cursor = conn.cursor()

    # cursor.execute(query, tuple_result)
    if select_count() == 0:
        cursor.execute(query, tuple_result)
    else:
        if to_db() == date:
            pass
        else:
            cursor.execute(query, tuple_result)
    print('커서클로즈')
    cursor.close()
    conn.commit()
    conn.close()

# oracle_controller.py
#
# import common.oracle_db as oradb
#
#
# def select_count():
#     conn = oradb.connect()
#     cursor = None
#     dict = []
#     query = 'select count(*) from covid'
#     try:
#         cursor = conn.cursor()
#         result = cursor.execute(query)
#         for row in result:
#             dict = row[0]
#     except Exception as msg:
#         print('select_count() 에러 발생 : ', msg)
#     finally:
#         cursor.close()
#         oradb.close(conn)
#     return dict
#
#
# def select_date_check(date):
#     conn = oradb.connect()
#     cursor = None
#     num = []
#     query = """SELECT TO_CHAR(COVID_DATE, 'YYYY/MM/DD') FROM COVID"""
#     try:
#         cursor = conn.cursor()
#         result = cursor.execute(query)
#         for row in result:
#             num.append(row[0])
#     except Exception as msg:
#         print('select_date() 에러 발생 : ', msg)
#     finally:
#         cursor.close()
#         oradb.close(conn)
#     if date in num:
#         return True
#     else:
#         return False
#
#
# def insert(tp_notice):
#     conn = oradb.connect()
#     cursor = None
#     query = """INSERT INTO COVID VALUES (TO_CHAR(SYSDATE, 'YY/MM/DD HH24/MI/SS'), :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, TO_DATE(:12))"""
#     try:
#         cursor = conn.cursor()
#         cursor.execute(query, tp_notice)
#         oradb.commit(conn)
#     except Exception as msg:
#         oradb.rollback(conn)
#         print('Notice insert() 에러 발생 : ' + msg)
#     finally:
#         cursor.close()
#         oradb.close(conn)
#
#
# def database(list):
#     print('DB inserting...')
#     db_list = []
#
#     for i in list[0][0][0]:
#         db_list.append(i)
#     for i in list[0][1][0]:
#         db_list.append(i)
#
#     for i in range(0, len(db_list)):
#         db_list[i] = db_list[i].replace(',', '')
#
#     db_list.append(list[1][0].replace('(', '').replace('.00시 기준)', '').replace('.', '/'))
#
#     if select_count() == 0:
#         print('DB inserting OK')
#         insert(db_list)
#     else:
#         if select_date_check(db_list[-1]):
#             print('DB inserting Pass')
#             pass
#         else:
#             print('DB inserting OK')
#             insert(db_list)