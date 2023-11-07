from flask import flash, request, render_template, redirect, session
from flask_app import app
from flask_app.models.equipment import Equipment
from flask_app.models.company import Company

@app.route('/equipment/create_equipment', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        data = {
            "company_id": session["company_id"],
            "scope_of_work" :request.form["scope_of_work"],
            "equipment_type": request.form["equipment_type"],
            "equipment_name": request.form["equipment_name"],
            "equipment_number": request.form["equipment_number"],
        }
        company_id = session['company_id']
        Equipment.equipment_save(data)
        return redirect(f'/equipment/view_all_equipment/{company_id}')
    
    return render_template('/equipment/create_equipment.html')

@app.route('/equipment/edit_equipment/<int:equipment_id>', methods=['GET', 'POST'])
def edit_equipment(equipment_id):
    if request.method == 'POST':
        data = {
            "id": equipment_id,
            "scope_of_work" : request.form["scope_of_work"],
            "equipment_type": request.form["equipment_type"],
            "equipment_name": request.form["equipment_name"],
            "equipment_number": request.form["equipment_number"],
        }

        Equipment.equipment_update(data)
        return redirect(f'/equipment/view_all_equipment/{session["company_id"]}')
    
    data = {"id": equipment_id}
    equipment = Equipment.get_one_equipment(data)
    return render_template('/equipment/edit_equipment.html', equipment=equipment)

@app.route('/equipment/view_all_equipment/<int:company_id>')
def get_all_equipment(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_equipment_per_company(data)
    company = Company.get_company_by_id(company_id)
    return render_template('/equipment/all_equipment.html', equipment=equipment, company = company)

# routes to get specific equipment per user

@app.route('/equipment/equipment_dashboard/<int:company_id>')
def show_equipment_dashboard(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_equipment_per_company(data)
    company = Company.get_company_by_id(company_id)
    return render_template('/equipment/equipment_dashboard.html', equipment=equipment, company = company)

@app.route('/equipment/view_exchangers/<int:company_id>')
def get_exchangers(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_exchangers_per_company(data)
    company = Company.get_company_by_id(company_id)
    equipment_type = "Exchangers"
    return render_template('/equipment/get_equipment.html', equipment=equipment, company = company, equipment_type = equipment_type)

@app.route('/equipment/view_drums/<int:company_id>')
def get_drums(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_drums_per_company(data)
    company = Company.get_company_by_id(company_id)
    equipment_type = "Drums"
    return render_template('/equipment/get_equipment.html', equipment=equipment, company = company, equipment_type = equipment_type)

@app.route('/equipment/view_tower_reactor/<int:company_id>')
def get_tower_reactors(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_towers_reactors_per_company(data)
    company = Company.get_company_by_id(company_id)
    equipment_type = "Towers / Reactors"
    return render_template('/equipment/get_equipment.html', equipment=equipment, company = company, equipment_type = equipment_type)

@app.route('/equipment/view_heaters/<int:company_id>')
def get_heaters(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_heaters_per_company(data)
    company = Company.get_company_by_id(company_id)
    equipment_type = "Heaters"
    return render_template('/equipment/get_equipment.html', equipment=equipment, company = company, equipment_type = equipment_type)

@app.route('/equipment/view_piping/<int:company_id>')
def get_piping(company_id):
    data = {"company_id": company_id}
    equipment = Equipment.get_all_piping_per_company(data)
    company = Company.get_company_by_id(company_id)
    equipment_type = "Piping"
    return render_template('/equipment/get_equipment.html', equipment=equipment, company = company, equipment_type = equipment_type)


