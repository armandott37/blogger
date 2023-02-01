import mysql.connector
from datetime import datetime

# class connection database Blogger

class Connection_db:
        
    # Connector to Database Container Mysql blogger_db
    def connector_db():
        connector_db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', port='23306', database='blogger_db')
        return connector_db
        
        
    # Insert into Database a Comment    
    def sql_add_comment(comment):
        connector_db = Connection_db.connector_db()        
        sql = f"INSERT INTO comments(comment_user, comment_datetime, comment_title, comment_contain) VALUES('{comment['comment_user']}', '{str(datetime.now())}', '{comment['comment_title']}', '{comment['comment_contain']}')"
        print(sql)        
        connector_db.cursor().execute(sql)
        connector_db.commit()
    
    # Update into Database a Comment    
    def sql_update_comment(comment):
        connector_db = Connection_db.connector_db()        
        sql = f"UPDATE comments SET comment_user = '{comment['comment_user']}', comment_datetime = '{datetime.now()}', comment_title = '{comment['comment_title']}', comment_contain = '{comment['comment_contain']}' WHERE comment_id = {comment['comment_id']})"
        print(sql)        
        connector_db.cursor().execute(sql)
        connector_db.commit()

    # Delete comment into Database a comment_id
    def sql_delete_comment(comment_id):
        connector_db = Connection_db.connector_db()        
        sql = f"DELETE FROM comments WHERE comment_id = {comment_id}"
        print(sql)        
        connector_db.cursor().execute(sql)
        connector_db.commit()

    # Get a Comment list data from Database a comment_id
    def sql_get_comment_for_id(comment_id):
        connector_db = Connection_db.connector_db()        
        sql = f"SELECT * FROM comments WHERE comment_id ='{comment_id}'"
        print(sql)
        cursor_db = connector_db.cursor()
        cursor_db.execute(sql)
        comment_sql = cursor_db.fetchone()        
        return comment_sql    
    
