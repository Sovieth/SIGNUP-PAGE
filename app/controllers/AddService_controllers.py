# /controllers
from flask import request, redirect, url_for, render_template
# from bson.objectId import ObjectId
from ..models.AddService_model import get_service

def AddService():
    if request.method == 'POST':
        category = request.form['category']
        price = request.form['price']
        description = request.form['description']
        image = request.files['image']

        services = {
            'category': category,
            'price': price,
            'description': description,
            'image': image.filename
        }
    
        get_service.Add_Service(services)
        return redirect(url_for('service_bp.services'))
    else:
        return render_template("AddService.html")

def services():
    services = get_service.getall_services()
    return render_template("ViewServices.html", services=services)

def delete_service():
    if request.method == "POST":
       id = request.form["id"]
       print("hjk", id)
       service_id = id
       get_service.delete_service(service_id)
    return redirect(url_for('service_bp.services'))

def  edit1_service():
    if request.method == "POST":
        id = request.form["id"]
        category = request.form.get("category")
        price = request.form.get("price")
        description = request.form.get("description")
        image = request.files['image']
    
        
        
        service = {
            'category': category,
            'price': price,
            'description': description,
            'image': image.filename
        }
        get_service.edit_service1(id, service)
        
        return redirect(url_for('service_bp.services'))
    else:
        return render_template("ViewServices.html", services=service)
    
  
def edit_service():
    if request.method == "POST":
        id = request.form["id"]
        category = request.form.get("category")
        price = request.form.get("price")
        description = request.form.get("description")
        image = request.form.get('image')
        print(id)
        print(category)
        print(price)
        print(description)
        print(image)
        return render_template('UpdateService.html', id=id,category=category, price=price, description=description)

    
    