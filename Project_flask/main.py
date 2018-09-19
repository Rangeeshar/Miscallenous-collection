from flask import *
from jira.client import JIRA
import urllib3
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
		try:
			urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
			jira = JIRA(basic_auth=(user,passw),options={'server':'https://182.76.223.10:6060/','verify':False},max_retries=0)
			issue = jira.issue('UN-9')
			if jira.current_user():
				response = redirect('http://54.174.153.99:9000')
				response.headers = {'Authorization': '%s'%(jira.current_user())}  
				return response
		except:
			return 'sorry username or password incorrect' 
		
if __name__=='__main__':
	app.run()