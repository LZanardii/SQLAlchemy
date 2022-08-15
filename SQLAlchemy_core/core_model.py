import sqlalchemy as db

# Define e conecta ao banco de dados
engine = db.create_engine('sqlite:///core.db', echo=True)
conn = engine.connect()

# Objeto que gerencia os metadados do banco de dados
meta = db.schema.MetaData()

# Definição da tabela principal
students = db.Table(
  'student', meta,
   db.Column('id', db.Integer, primary_key=True),
   db.Column('name', db.String(100), nullable=False),
   db.Column('lastname', db.String(50)),
   db.Column('sex', db.String(1)),
   db.Column('age', db.SmallInteger),
)

# Definição da tabela secundária
addresses = db.Table(
   'address', meta, 
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('student_id', db.Integer, db.ForeignKey('student.id')), 
   db.Column('address', db.String), 
   db.Column('email', db.String))

# Cria a tabela no banco caso ela não exista
meta.create_all(engine)