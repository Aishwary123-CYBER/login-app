from flask import *  
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/upload"
app.config['SECRET_KEY'] = 'imsecret'

class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    data = db.Column(db.Binary)







@app.route('/')
def login():
    return render_template('login.html')

@app.route('/success',methods=['POST'])
def success():
    
    if request.method=='POST':
        session['name'] = request.form['name']
        password = request.form['pass']

    if password == password:
        resp = redirect(url_for('profile'))
        resp.set_cookie('name',session['name'])
        return resp

    else:
        return '<h1>Wrong password</h1>'

@app.route('/profile')
def profile():
    name = request.cookies.get("name")
    resp = make_response(render_template('profile.html',name=name))
    return resp

@app.route('/logout')
def logout():
    if 'name' in session:
        session.pop('name',None)
        return '<h1>Logout successfully</h1>'
    else:
        return abort(400)


@app.route('/file_upload')
def upload():
    return render_template('upload.html')

@app.route('/successs',methods=['POST'])
def successs():
        f = request.files['file']
        newfile = Data(name=f.filename,data=f.read())
        db.session.add('newfile')
        db.session.commit()

        return f"{f.filename} is saved"
        










 

  
if __name__ == "__main__":  
    app.run(debug = True)  