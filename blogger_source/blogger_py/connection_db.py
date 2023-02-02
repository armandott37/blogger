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
    
    # Insert into Database a Response    
    def sql_add_response(response):
        connector_db = Connection_db.connector_db()        
        sql = f"INSERT INTO responses(response_user, response_datetime, response_contain, comment_id) VALUES('{response['response_user']}', '{datetime.now()}', '{response['response_contain']}', '{response['comment_id']}')"
        print(sql)        
        connector_db.cursor().execute(sql)
        connector_db.commit()
    
    # Update into Database a Response
    def sql_update_response(response):
        connector_db = Connection_db.connector_db()        
        sql = f"UPDATE reponses SET response_user = '{response['response_user']}', response_datetime = '{datetime.now()}', response_contain = '{response['response_contain']}', comment_id = '{response['comment_id']}' WHERE response_id = {response['response_id']})"
        print(sql)        
        connector_db.cursor().execute(sql)
        connector_db.commit()

    # Delete response into Database a response_id
    def sql_delete_response(response_id):
        connector_db = Connection_db.connector_db()        
        sql = f"DELETE FROM responses WHERE response_id = {response_id}"
        print(sql)        
        connector_db.cursor().execute(sql)
        connector_db.commit()

    # Get a Response list data from Database a response_id
    def sql_get_response_for_id(response_id):
        connector_db = Connection_db.connector_db()        
        sql = f"SELECT * FROM responses WHERE response_id ='{response_id}'"
        print(sql)
        cursor_db = connector_db.cursor()
        cursor_db.execute(sql)
        response_sql = cursor_db.fetchone()        
        return response_sql    
    
