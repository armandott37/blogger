from datetime import datetime
import connection_db as db

class Response:

    # Atributes class response
    response_id = 0    
    response_user = "Juan"
    response_datetime =  datetime.now()    
    response_contain = "Contain response"
    comment_id = 0

    # Constructor class Response
    def __init__(self, response_id, response_user, response_datetime, response_contain, comment_id):
        self.response_id = response_id
        self.response_user = response_user
        self.response_datetime = response_datetime        
        self.response_contain = response_contain
        self.comment_id = comment_id
    
    # Insert response into Database    
    def insert_db_response(response):        
        db.Connection_db.sql_add_response(response)
        print(response)
    
    def update_db_response(response):
        db.Connection_db.sql_update_response(response)
        return response
    
    # Delete a response into Database for response_id    
    def delete_db_response(response_id):
        db.Connection_db.sql_delete_response(response_id)
        return response_id
        
    # return list data response Database for response_id 
    def get_response_db_for_id(response_id):
        response_list = db.Connection_db.sql_get_response_for_id(response_id)
        return response_list
    
    # return Object response for response_id
    def get_response_id(response_id):
        response_list = Response.get_response_db_for_id(response_id)
        response = response(response_list[0], response_list[1], response_list[2], response_list[3], response_list[4])
        return response