import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time


def main():

    # title = st.text_input('책 제목 입력')
    # author_fname = st.text_input('이름 입력')
    # author_lname = st.text_input('성 입력')
    # released_year = st.number_input('년도 입력')
    # stock_quantity = st.number_input('수량 입력')
    # pages = st.number_input('페이지 입력')

    #####

    # name = st.text_input('이름 입력') 
    # birth_date = st.date_input('생년월일')
    # birth_time = st.time_input('시간입력')

    # birth_dt = datetime.combine(birth_date, birth_time)

    # print(birth_date)
    # print(birth_time)
    # print(birth_dt)

    #####

    if st.button('저장') :

        try :
            # 1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.ctcjv4wiezfo.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )

            if connection.is_connected() :
                print('연결됐을때')
                db_info = connection.get_server_info()
                print('MySQL server version : ', db_info)

                # 2. 커서를 가져온다.
                cursor = connection.cursor()

                # 3. 우리가 원하는거 실행 가능.
                #cursor.execute('select database();')

                query = '''insert into cats4 (name, age)
                    values( %s, %s );'''

                record = [ ('냐옹이',1),('나비',3), ('단비',5) ]
                print(datetime.now())
                cursor.executemany(query, record)
                connection.commit()
                print('{}개 적용됨'.format(cursor.rowcount))
                # 4. 실행 후 커서에서 결과를 빼낸다.
                # record = cursor.fetchone()
                # print('Connected to db : ', record)

        except Error as e :
            print('디비 관련 에러 발생', e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')

        
if __name__ == '__main__' :
    main()