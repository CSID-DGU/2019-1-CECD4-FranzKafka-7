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

def end_game():
    #똑 ! 딱! 
    conn.close()



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
        cursor.execute(sql, keyword)
        result = cursor.fetchone()

        return result['p_date']

    def set_data(keyword, data_list):
        sql = '''
        INSERT IGNORE INTO sns (keyword, content, p_date, created_at, updated_at) VALUES (%s, %s, %s, now(), now())
        '''
        cursor.executemany(sql,data_list)

        return conn.insert_id()
        
class TwitterMetadata:
    def is_overlap(data_list):
        for i in data_list:
            if check_exist(i):
                return False
        return True        
        
    def check_exist(item_id):
        sql = '''
        SELECT  `twitter_metadata`.* FROM `twitter_metadata` 
        WHERE `twitter_metadata`.`item_id` = %s 
        '''
        if cursor.execute(sql, item_id)!=0:
            return True
        else:
            return False


    def set_data(first_id, data_list):
        sql = '''
        INSERT INTO `twitter_metadata` 
        (`item_id`, `user_data_name`, `user_screen_name`, `user_id`, `sns_id`, `created_at`, `updated_at`) 
        VALUES (%s, %s, %s, %s, 1, now(), now())
        '''

        for idx , val in enumerate(range(first_id,first_id+len(data_list))):
            data_list[idx].append(val)
        cursor.executemany(sql,data_list)

        cursor.connection.commit()




