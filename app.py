#source my-env-/bin/activate
#pip install flask, flask-sqlalchemy, jinja2

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# //// absolute path
# /// relative path
db = SQLAlchemy(app)

# creating DB
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# POST GET
@app.route('/', methods=['POST', 'GET']) #with post/get we can send data to db
def index():
    if request.method == 'POST':
        task_content = request.form['content'] #from content input box
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was mistake adding your task'
        
    else:
        #tasks = Todo.query.order_by(Todo.date.date_created).first()
        tasks = Todo.query.order_by(Todo.date_created).all()
        #going to look at all db content, and return with order created
        return render_template('index.html', tasks=tasks) 
    #it knows that the file is in templates

# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    #attempt to get task by id, if it doesnt exist it will return 404 
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

# UPDATE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem  updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)


