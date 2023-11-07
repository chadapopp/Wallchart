from flask import flash, request, render_template, redirect, session
from flask_app import app
from flask_app.models.company import Company
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
app.secret_key = "whateveritis"

@app.route('/register_company')
def register_company_form():
    return render_template('/company/register_company.html')

@app.route('/login_company')
def login_company_form():
    return render_template('/company/login_company.html')

@app.route('/company_dashboard/<int:company_id>')
def company_main_page(company_id):
    company = Company.get_company_by_id(company_id)
    if not company:
        flash("Invalid Company ID")
        return redirect('/register_company')

    return render_template('/company/company_dashboard.html', company=company)


@app.route('/create_company', methods = ["POST"])
def create_company():
    pw_hash = bcrypt.generate_password_hash(request.form['company_password'])
    data = {
        "admin_name": request.form["admin_name"],
        "company_name" : request.form["company_name"],
        "company_password" : pw_hash
    }
    company_id = Company.save_company(data)
    return redirect(f'/company_dashboard/{company_id}')

@app.route('/company_login', methods=['POST'])
def admin_login():
    admin_name = request.form['admin_name']
    company_password = request.form['company_password']
    company = Company.get_company_admin({"admin_name": admin_name})
    if not company:
        flash("Invalid Admin Name")
        return redirect('/register_company')

    if not bcrypt.check_password_hash(company.company_password, company_password):
        flash("Invalid Company Password")
        return redirect('/register_company')
    
    session['company_id'] = company.id
    session['admin_name'] = company.admin_name
    session['company_name'] = company.company_name
    print(session['company_name'])

    return redirect(f'/company_dashboard/{company.id}')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')