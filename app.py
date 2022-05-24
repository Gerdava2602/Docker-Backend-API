from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Sequence, create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from datetime import datetime
from datetime import timedelta
import json


app = Flask(__name__)
conn_string = 'sqlite:///auth.db'
app.config["SQLALCHEMY_DATABASE_URI"] = conn_string
engine = create_engine(conn_string)

db = SQLAlchemy(app)

class s(db.Model):
    __tablename__= 's'
    
    id = Column(Integer, primary_key=True)
    hash = Column(String)
    timestamp = Column(DateTime)
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}        
    
    def __repr__(self):
        return f'id: {self.id}, hash: {self.hash}, timestamp: {self.timestamp}'
    
    
class a(db.Model):
    __tablename__= 'a'
    
    test = Column(Integer, Sequence('id_seq', start=1), primary_key=True)
    id = Column(Integer)
    hash = Column(String)
    timestamp = Column(DateTime)
    answer = Column(String)
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
            
    def __repr__(self):
        return f'id: {self.id}, hash: {self.hash}, timestamp: {self.timestamp}, answer: {self.answer}'
    


@app.route('/')
def index():
    try:
        with Session(engine) as session:
            return 'ok'
    except Exception as e:
        return 'nok'
    

@app.route('/user/<id>')
def user(id: int):
    now = datetime.now()
    h = hash(now)
    reg = s(id=id, hash=h, timestamp=now)
    try:
        with Session(engine) as session:
            session.add(reg)
            session.commit()
        return str(h)
    except Exception as e:
        print(e)
        return 'nok'
    
    
@app.route('/user/<id>/<hash>')
def user2(id: int, hash: str):
    now = datetime.now()
    with Session(engine) as session:
        check = session.query(s).filter(s.hash==hash).one_or_none()
        if not check: return 'nok' #If hash not on table
        if (check.timestamp + timedelta(hours=4)) >= datetime.now():
            record = a(id=check.id, hash=check.hash, timestamp=datetime.now(), answer='ok')
            session.add(record)
            session.commit()
            return 'ok'
        
        record = a(id=check.id, hash=check.hash, timestamp=datetime.now(), answer='nok')
        session.add(record)
        session.commit()
        return 'nok'
    
        
@app.route('/delete')
def delete():
    with Session(engine) as session:
        session.query(a).delete()
        session.query(s).delete()
        session.commit()
    return 'ok'


@app.route('/a')
def jsona():
    with Session(engine) as session:
        data = session.query(a).all()
        return json.dumps([d.as_dict() for d in data])
    
    
@app.route('/s')
def jsons():
    with Session(engine) as session:
        data = session.query(s).all()
        return json.dumps([d.as_dict() for d in data])
    

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(host='0.0.0.0:4000', debug=True)