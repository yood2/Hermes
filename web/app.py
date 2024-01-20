from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Primary key that is an integer
    content = db.Column(db.String(200), nullable=False) #Cannot be null, cap of 200
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #Use datetime library for datetime objects

    def __repr__(self):
        return '<Task %r>' % self.id




#Can be called in CLI with 'flask create-db'
@app.cli.command("create-db")
def create_db():
    db.create_all()
    print("Database tables created")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'] #task_content becomes the input in the form id='content'
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)