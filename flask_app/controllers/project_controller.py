from flask import flash, request, render_template, redirect, session
from flask_app import app
from flask_app.models.equipment import Equipment
from flask_app.models.company import Company
from flask_app.models.project import Projects

@app.route('/projects/dashboard/<int:company_id>')
def wallchart_dashboard(company_id):
    company = Company.get_company_by_id(company_id)
    return render_template('/projects/project_dashboard.html', company = company)

@app.route('/projects/create_project', methods = ['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        data = {
            "company_id": session['company_id'],
            "project_name": request.form["project_name"],
            "project_city": request.form["project_city"],
            "project_state": request.form["project_state"],
            "project_start_date": request.form["project_start_date"],
            "project_end_date": request.form["project_end_date"]
        }
        company_id = session['company_id']
        Projects.project_save(data)
        return redirect(f'/projects/view_all_projects/{company_id}')
    return render_template('/projects/create_project.html')

@app.route('/projects/view_all_projects/<int:company_id>')
def view_all_projects_by_company(company_id):
    data = {"company_id": company_id}
    projects = Projects.view_all_projects_per_company(data)
    company = Company.get_company_by_id(company_id)
    return render_template('/projects/view_all_projects.html', projects = projects, company = company)