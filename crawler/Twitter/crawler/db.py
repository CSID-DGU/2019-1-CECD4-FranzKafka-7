import pymysql;
import os;
import sys;



try:
    conn = pymysql.connect(
    host="",
    port=3306,
    user='root',
    passwd=os.environ['MYSQL_PASS'],
    db='twitter_development',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
except pymysql.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit()


class Keyword:
    def get():
        sql = '''
        SELECT  `keywords`.* FROM `keywords` WHERE `keywords`.`active` = TRUE
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
        print('search keywords : ',[i['word'] for i in result])
        return [ i['id'] for i in result ]

class Sns:
    def last_date(keyword):
        sql = '''
        SELECT  `sns`.* FROM `sns` WHERE `sns`.`keyword_id` = %s 
        ORDER BY `sns`.`p_date` DESC LIMIT 1
        '''
        cursor.execute(sql)
        result = cursor.fetchone()
        


