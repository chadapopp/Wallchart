from flask_app.config.mysqlconnection import connectToMySQL

class Projects:
    DB = 'wallchart_schema'
    def __init__(self, wallchart_data):
        self.id =  wallchart_data['id']
        self.company_id =  wallchart_data['company_id']
        self.equipment_id = wallchart_data['equipment_id']
        self.project_name = wallchart_data['project_name']
        self.project_city =  wallchart_data['project_city']
        self.project_state =  wallchart_data['project_state']
        self.project_start_date =  wallchart_data['project_start_date']
        self.project_end_date =  wallchart_data['project_end_date']
        self.created_at =  wallchart_data['created_at']
        self.updated_at =  wallchart_data['updated_at']
    
    @classmethod
    def project_save(cls,data):
        query = "INSERT INTO projects (company_id, project_name, project_city, project_state, project_start_date, project_end_date) VALUES (%(company_id)s, %(project_name)s, %(project_city)s, %(project_state)s, %(project_start_date)s,%(project_end_date)s)"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def view_all_projects_per_company(cls, data):
        query = "SELECT * FROM projects WHERE company_id = %(company_id)s"
        results = connectToMySQL(cls.DB).query_db(query, data)
        projects = []
        for row in results:
            projects.append(cls(row))
        return projects