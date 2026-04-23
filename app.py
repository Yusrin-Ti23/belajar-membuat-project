from flask import Flask, render_template

app = Flask(__name__)

# Data produk
produk = [
    {"nama": "Sayur Bayam", "kategori": "Sayur", "harga": 5000},
    {"nama": "Apel Merah", "kategori": "Buah", "harga": 10000},
    {"nama": "Ikan Tuna", "kategori": "Ikan", "harga": 25000}
]

@app.route("/")
def home():
    return render_template("index.html", produk=produk)

@app.route("/produk")
def produk_page():
    return render_template("produk.html", produk=produk)

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

if __name__ == "__main__":
    app.run(debug=True)