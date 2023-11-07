from flask_app.config.mysqlconnection import connectToMySQL

class Company:
    DB = "wallchart_schema"
    def __init__(self, company_dict):
        self.id = company_dict["id"]
        self.admin_name = company_dict["admin_name"]
        self.company_name = company_dict["company_name"]
        self.company_password = company_dict["company_password"]
        self.created_at = company_dict["created_at"]
        self.updated_at = company_dict["updated_at"]

    @classmethod
    def save_company(cls, data):
        query = """INSERT INTO companies (company_name, admin_name, company_password) VALUES (%(company_name)s, %(admin_name)s, %(company_password)s)"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_company_admin(cls, data):
        query = """SELECT * FROM companies WHERE admin_name = %(admin_name)s"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    # write a function to get the name of the company by the company id
    @classmethod
    def get_company_by_id(cls, id):
        query = "SELECT * FROM companies WHERE id = %(id)s"
        data = {"id": id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None
