from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model.model import test_table
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate()
db.init_app(app)
db.create_all() 

migrate.init_app(app, db)

@app.route('/insert', methods = ['POST'] )
def insert_data():
    text_data = request.args.get("text")
    new_task = test_table(text=text_data)

    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/') # 메인 화면으로 리다이렉트
    except:
        return "There was an issue adding your task."

@app.route('/api', methods = ['GET'])
def get_data():
    data = test_table.query.all()
    return render_template("api.html", data=data)

@app.route('/', methods=['GET'])
def index(): 
    return "Hello World on Docker!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')