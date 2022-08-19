import sqlalchemy as db
import sqlalchemy.orm as orm
from model import *

engine = db.create_engine(DATABASE_CONNECTION, echo=True)
conn = engine.connect()

Session = orm.sessionmaker(bind=engine)
session = Session()

try:
  rows = [
    Pessoa(nome="Pedro", sexo="M", salario=3800, idade=35, veiculos=[Veiculo(fabricante="Fiat", modelo="Uno", ano=2017)]), 
    Pessoa(nome="Maria", sexo="F", salario=2750, idade=23, veiculos = [Veiculo(fabricante="Chevrolet", modelo="Onix", ano=2016), Veiculo(fabricante="Fiat", modelo="Mobi", ano=2020)]),
    Pessoa(nome="Roberto", sexo="M", salario=4210, idade=36, veiculos= [Veiculo(fabricante="Ford", modelo="Fiesta", ano=2013)]), 
    Pessoa(nome="Sandra", sexo="F", salario=2695, idade=27, veiculos = [Veiculo(fabricante="VW", modelo="Gol", ano=2019), Veiculo(fabricante="Ford", modelo="Ka", ano=2014)]),
    Pessoa(nome="Camila", sexo="F", salario=6170, idade=42, veiculos=[Veiculo(fabricante="VW", modelo="Up", ano=2018)])
  ]
  session.add_all(rows)
  session.commit()  

except Exception as e:
    session.rollback()
    print(e)

session.close()
conn.close()
engine.dispose()