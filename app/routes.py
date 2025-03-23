from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)
from app import db, app

# Pages
@app.route('/')
@app.route('/index')
def index():
    # Ambil Halaman HTML Home
    return render_template('index.html')


@app.route('/items')
def lihatBarang():
    documents = db.collection("Inventori").get()
    arr_data = []
    for doc in documents:
        data = doc.to_dict() # Convert document to dictionary
        data["id"] = doc.id
        arr_data.append(data)
    
    return render_template("read-item.html", arr_data=arr_data)