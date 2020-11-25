from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<id>:<password>@localhost:3306/<db name>'

db = SQLAlchemy(app)

class MyTable(db.Model):
    id = Column(db.Integer, nullable=False, primary_key=True)
    value = Column(db.String(40), nullable=False, default='')


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/select')
def select():
    row_id = request.args.get('id', type=int)
    row = MyTable.query.filter_by(id=row_id).first()
    return (row.value, 200) if row else ('', 400)


@app.route('/insert', methods=['POST'])
def insert():
    value = request.form.get('value', type=str)
    row = MyTable(value=value)
    db.session.add(row)
    db.session.commit()
    return ('ok', 200)


if __name__ == "__main__":
    app.run('0.0.0.0', port=3306)
