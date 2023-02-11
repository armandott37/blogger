from datetime import datetime
import connection_db as db

class Comment:

    # Atributes class Comment
    comment_id = 0
    comment_user = "Juan"
    comment_datetime =  datetime.now()
    comment_title = "Title comment"
    comment_contain = "Contain comment"    

    # Constructor class Comment
    def __init__(self, comment_id, comment_user, comment_datetime, comment_title, comment_contain):
        self.comment_id = comment_id
        self.comment_user = comment_user
        self.comment_datetime = comment_datetime
        self.comment_title = comment_title
        self.comment_contain = comment_contain
    
    # Insert comment into Database    
    def insert_db_comment(comment):        
        db.Connection_db.sql_add_comment(comment)
        print(comment)
    
    def update_db_comment(comment):
        db.Connection_db.sql_update_comment(comment)
        return comment
    
    # Delete a comment into Database for comment_id    
    def delete_db_comment(comment_id):
        db.Connection_db.sql_delete_comment(comment_id)
        return comment_id
        
    # return list data Comment Database for comment_id 
    def get_comment_db_for_id(comment_id):
        comment_list = db.Connection_db.sql_get_comment_for_id(comment_id)
        return comment_list
    
    # return Object Comment for comment_id
    def get_comment_id(comment_id):
        comment_list = Comment.get_comment_db_for_id(comment_id)
        comment = Comment(comment_list[0], comment_list[1], comment_list[2], comment_list[3], comment_list[4])
        return comment
        
        

        
