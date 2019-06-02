# -*- coding: utf-8 -*-
import pymysql;
import os;
import sys;
import pdb;
import datetime as dt;


try:
    conn = pymysql.connect(
    host="",
    port=3306,
    user='root',
    passwd=os.environ['MYSQL_PASS'],
    db='twitter_development',
    charset='utf8mb4',
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
        return [ {'id' : i['id'], 'word' : i['word'], 'end_date' : i['end_date'].date()} for i in result ]

class Sns:
    def last_date(keyword):
        sql = '''
        SELECT  `sns`.* FROM `sns` WHERE `sns`.`keyword_id` = %s 
        ORDER BY `sns`.`p_date` DESC LIMIT 1
        '''
        cursor.execute(sql, keyword)
        result = cursor.fetchone()
        if result is None:
            return dt.datetime.now().date()
        else:
            return result['p_date'].date()

    def save(data_list):
        sql = '''
        INSERT IGNORE INTO sns (keyword_id, content, p_date, created_at, updated_at) VALUES (%s, %s, %s, now(), now())
        '''
        cursor.executemany(sql, data_list)

        return conn.insert_id()
        
class TwitterMetadata:
    def check_overlap(data_list):
        # (data-item-id, data-name, data-screen-name...) 형식으로 되어있다.
        for i in data_list:
            if is_exist(i[0]):
                return False
        return True        
        
    def is_exist(item_id):
        sql = '''
        SELECT  `twitter_metadata`.* FROM `twitter_metadata` 
        WHERE `twitter_metadata`.`item_id` = %s 
        '''
        if cursor.execute(sql, item_id)!=0:
            return True
        else:
            return False


    def save(first_id, data_list):
        
        sql = '''
        INSERT INTO `twitter_metadata` 
        (`item_id`, `user_data_name`, `user_screen_name`, `user_id`, `sns_id`, `created_at`, `updated_at`) 
        VALUES (%s, %s, %s, %s, %s, now(), now())
        '''
        

        for idx , val in enumerate(range(first_id-len(data_list) + 1, first_id + 1)):
            data_list[idx] = data_list[idx] + (val,)
        
        cursor.executemany(sql,data_list)

        cursor.connection.commit()




