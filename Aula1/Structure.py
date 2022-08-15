import sqlalchemy as db
import sqlalchemy.orm as orm

DATABASE_CONNECTION = "sqlite:///atividade_1.db"

engine = db.create_engine(DATABASE_CONNECTION, echo=True)
conn = engine.connect()
Base = orm.declarative_base()

class Pessoa(Base):
  __tablename__ = 'pessoa'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String)
  sexo = db.Column(db.String)
  salario = db.Column(db.Float)
  idade = db.Column(db.Integer)
  id_veiculo = db.Column(db.Integer, db.ForeignKey("veiculo.id"))

class Veiculo(Base):
  __tablename__ = 'veiculo'
  id = db.Column(db.Integer, primary_key=True)
  fabricante = db.Column(db.String)
  modelo = db.Column(db.String)
  ano = db.Column(db.Integer)

Base.metadata.create_all(engine)
conn.close()


