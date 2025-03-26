from flask import Blueprint, render_template, redirect, request

routes = Blueprint("routes", __name__)
from app import db, app
import uuid

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


@app.route('/add-item')
def tambahBarang():
    # UUID Generator -> Kapital -> Potong 10 Karakter
    item_id = str(uuid.uuid4()).replace("-","").upper()[0:10]
    # Tampilkan HTML dengan Return
    return render_template("add-item.html", id=item_id)


@app.route('/send-data', methods=["POST"])
def kirimData():
    # get data from form
    idBarang = str(request.form.get('id'))
    namaBarang = str(request.form.get('nama'))
    jumlahBarang = str(request.form.get('jumlah'))
    deskripsiBarang = str(request.form.get('deskripsi'))
    # Masukkan ke Struktur Data
    data = {
        'id': idBarang,
        'nama': namaBarang,
        'jumlah': jumlahBarang,
        'deskripsi': deskripsiBarang
    }
    # Database Query
    db.collection('Inventori').document('Doc-'+idBarang).set(data)
    # display item list
    return redirect("/items")


@app.route('/update-item')
def ubahBarang():
    # Ambil ID Barang dari GET Request
    idBarang = request.args.get('idbarang')

    # Ambil Data di Database
    data = db.collection("Inventori").document(idBarang).get().to_dict()
    
    # Tampilkan HTML dengan Return
    return render_template("update-item.html", data=data)

@app.route('/updated', methods=["POST"])
def kirimPerubahan():
    # Ambil Data dari Form
    idBarang = str(request.form.get('id'))
    namaBarang = str(request.form.get('nama'))
    jumlahBarang = str(request.form.get('jumlah'))
    deskripsiBarang = str(request.form.get('deskripsi'))
    # Masukkan ke Struktur Data
    data = {
        'id': idBarang,
        'nama': namaBarang,
        'jumlah': jumlahBarang,
        'deskripsi': deskripsiBarang
    }
    # Kueri ke Database
    db.collection('Inventori').document('Doc-'+idBarang).set(data)
    # Tampilkan Lihat Barang
    return redirect("/items")