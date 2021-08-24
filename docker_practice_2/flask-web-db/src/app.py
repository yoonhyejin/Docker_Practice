from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from model.model import Todo
import config
#import pymysql

#pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Todo(db.Model): # Initialize DB model
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return 'Task %r' % self.id # 새로 생성할때마다 task id를 리턴한다

@app.route('/insert', methods = ['POST'] )
def insert_data():
    id_data = request.args.get("id")
    text_data = request.args.get("text")
    new_task = Todo(id=id_data, text=text_data)

    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/') # 메인 화면으로 리다이렉트
    except:
        return "There was an issue adding your task."




@app.route('/api', methods = ['GET'])
def get_data():
    data = Todo.query.all()
    return render_template("api.html", data=data)

@app.route('/', methods=['GET'])
def index(): 
    # return render_template('index.html')
    return "Hello World on Docker!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')