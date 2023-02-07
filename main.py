from flask import Flask, request,render_template
from sorgu import sorgu

app = Flask(__name__)

@app.route('/')
def index():
   return  render_template('/index.html')

   

@app.route('/', methods=['POST'])
def form_submit():
   isim = str(request.form['isim'])
   soyisim = str(request.form['soyisim'])

   son_durum = sorgu(isim,soyisim)


   return son_durum

if __name__ == '__main__':
   app.run(debug=True)