#file home.py
#contoh halaman web dengan flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  pengguna = {'username': 'Iqbal'}
  posting = [
		{
			'pengarang': {'username': 'Nama Pengarang'},
			'tulisan': 'Pemandangan di Pantai Jetis yang sangat indah ..'
		},
		{
			'judul': {'username': 'Judul Lengkap'},
			'tulisan': 'Film The Avengers bagus sekali ..'
		},
		{
			'penerbit': {'username': 'Penerbit'},
			'tulisan': 'Film The Avengers bagus sekali ..'
		},
		{
			'tahun': {'username': 'Tahun'},
			'tulisan': 'Film The Avengers bagus sekali ..'
		}
  ]
  return render_template('index.html', title='Home', user=pengguna, posts=posting)		