from flask import flash, request, render_template, redirect, session
from flask_app import app
from flask_app.models.company import Company
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



@app.route('/admin/add_user')
def admin_user_create():
    if 'company_id' not in session:
        flash('Company ID not found in session')
        return redirect('/register_company')
    company_info = Company.get_company_by_id(id=session['company_id'])
    return render_template('/users/create_user.html', company_info=company_info)

@app.route('/admin/add_user/create', methods=['POST'])
def create_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "company_id": session['company_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" :pw_hash,
    }
    company_id = session["company_id"]
    User.create_user(data)  
    return redirect(f'/users/all_users/{company_id}')

@app.route('/users/all_users/<int:company_id>')
def show_all_users_per_company(company_id):
    company_info = Company.get_company_by_id(id=company_id)
    all_users = User.get_all_users_per_company(company_id)
    return render_template('/users/all_users.html', all_users=all_users, company_info=company_info)

@app.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "id": user_id,
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash,
        }
        User.update_user(data)
        return redirect(f'/users/all_users/{session["company_id"]}')

    # Handle GET request
    user_info = User.get_user_by_id(user_id)
    company_info = Company.get_company_by_id(id=session['company_id'])
    return render_template('/users/edit_user.html', user=user_info, company_info=company_info)

@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):   
    User.delete_user(user_id)
    return redirect(f'/users/all_users/{session["company_id"]}')
