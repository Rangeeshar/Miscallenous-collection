from flask import *
app=Flask(__name__)
@app.route('/')
def index():
	return redirect(url_for('login'))
@app.route('/home')
def login():
	return render_template('index.html')
@app.route('/validate_user',methods=['POST','GET'])
def validate():
	if request.method =='POST':
		user=request.form.get('username')
		passw=request.form.get('pass')
		return user+" "+passw
	
if __name__=='__main__':
	app.run()