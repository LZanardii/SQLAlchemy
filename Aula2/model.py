import sqlalchemy as db
import sqlalchemy.orm as orm

DATABASE_CONNECTION = "sqlite:///atividade_2.db"

engine = db.create_engine(DATABASE_CONNECTION)
conn = engine.connect()
Base = orm.declarative_base()

class Pessoa(Base):
  __tablename__ = 'pessoa'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String)
  sexo = db.Column(db.String)
  salario = db.Column(db.Float)
  idade = db.Column(db.Integer)
  
  # def __str__(self):
  #   text = f'Pessoa: {self.nome} {self.sexo} ({self.salario}) ({self.idade})\n '
  #   text += '\n  '.join([str(i) for i in self.veiculos])
  #   return text.strip()

class Veiculo(Base):
  __tablename__ = 'veiculo'
  id = db.Column(db.Integer, primary_key=True)
  id_pessoa = db.Column(db.Integer, db.ForeignKey("pessoa.id"))
  fabricante = db.Column(db.String)
  modelo = db.Column(db.String)
  ano = db.Column(db.Integer)

  # def __str__(self):
  #   text = f'Veiculo: {self.fabricante} {self.modelo} ({self.ano})\n '
  #   text += '\n  '.join([str(i) for i in self.pessoa])
  #   return text.strip()

Pessoa.veiculos = orm.relationship('Veiculo', back_populates='pessoa', cascade='all, delete')
Veiculo.pessoa = orm.relationship('Pessoa', back_populates='veiculos')

Base.metadata.create_all(engine)
conn.close()


