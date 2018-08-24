'''from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)'''
import requests as rq

val=rq.get('https://api.github.com/users/mralexgray/repos')
print(val.text)

