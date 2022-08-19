import sqlalchemy as db
import sqlalchemy.orm as orm
from structure import *

engine = db.create_engine(DATABASE_CONNECTION, echo=True)
conn = engine.connect()

Session = orm.sessionmaker(bind=engine)
session = Session()

rows = [
  Pessoa(nome="Pedro", sexo="M", salario=3800, idade=35, id_veiculo=2), 
  Pessoa(nome="Maria", sexo="F", salario=2750, idade=23, id_veiculo=1),
  Pessoa(nome="Roberto", sexo="M", salario=4210, idade=36, id_veiculo=3), 
  Pessoa(nome="Sandra", sexo="F", salario=2695, idade=27, id_veiculo=2),
  Pessoa(nome="Camila", sexo="F", salario=6170, idade=42, id_veiculo=3),
  Veiculo(fabricante="Chevrolet", modelo="Onix", ano=2016), 
  Veiculo(fabricante="Fiat", modelo="Mobi", ano=2020), 
  Veiculo(fabricante="Ford", modelo="Fiesta", ano=2013),
  Veiculo(fabricante="VW", modelo="Gol", ano=2019)
]

session.add_all(rows)
session.commit()
session.close()
conn.close()