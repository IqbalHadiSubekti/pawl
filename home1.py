#file home.py
#contoh halaman web dengan flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  pengguna = {'username': 'Iqbal'}
  posting = [
		{
			'penulis': {'username': 'Hadi'},
			'tulisan': 'Pemandangan di Pantai Jetis yang sangat indah ..'
		},
		{
			'penulis': {'username': 'Subekti'},
			'tulisan': 'Film The Avengers bagus sekali ..'
		}
  ]
  return render_template('index.html', title='Home', user=pengguna, posts=posting)
			