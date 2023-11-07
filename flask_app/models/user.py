from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "wallchart_schema"
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.company_id = user_dict["company_id"]
        self.first_name = user_dict["first_name"]
        self.last_name = user_dict["last_name"]
        self.email = user_dict["email"]
        self.password = user_dict["password"]
        self.created_at = user_dict["created_at"]
        self.updated_at = user_dict["updated_at"]

    # write a method to save a user to the database under the certain company name inputed from the admin
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (company_id, first_name, last_name, email, password) VALUES (%(company_id)s, %(first_name)s, %(last_name)s, %(email)s, %(password)s)"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all_users_per_company(cls, company_id):
        query = """SELECT * FROM users WHERE company_id = %(company_id)s"""
        data = {"company_id": company_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_user_by_id(cls, user_id):
        query = """SELECT * FROM users WHERE id = %(user_id)s"""
        data = {"user_id": user_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def delete_user(cls, user_id):
        query = """DELETE FROM users WHERE id = %(user_id)s"""
        data = {"user_id": user_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
