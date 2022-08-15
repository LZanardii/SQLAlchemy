from dataclasses import replace
import re
import sqlalchemy as db
import sqlalchemy.orm as orm
from Structure import *

engine = db.create_engine(DATABASE_CONNECTION)
conn = engine.connect()

Session = orm.sessionmaker(bind=engine)
session = Session()

print()

# Somatório dos salários dos homens
rows = session.query(db.func.sum(Pessoa.salario)).filter(Pessoa.sexo == 'M')
print("Soma dos salários dos homens com ORM -->", re.sub('[(]|[)]|[,]', '', str(rows[0])))
rows = session.query(Pessoa).all();
soma = 0
for r in rows:
  if (r.sexo == "M"):
    soma += r.salario
print("Soma dos salários dos homens com For -->", soma)   
print("Soma dos salários dos homens comprehension -->", sum([p.salario for p in rows if p.sexo == "M"]))   
print()

# Salário médio das mulheres
rows = session.query(db.func.sum(Pessoa.salario)/2).filter(Pessoa.sexo == 'F')
print("Salário médio das mulheres --> ", re.sub('[(]|[)]|[,]', '', str(rows[0])))
print()

# Nome da pessoa, fabricante e modelo do veículo que ela possui
rows = session.query(Pessoa.nome, Veiculo.fabricante, Veiculo.modelo ).filter(Pessoa.id_veiculo == Veiculo.id)
print("Nome da pessoa, fabricante e modelo do veículo que ela possui: ")
for r in rows:
  print("| {:<7} | {:<9} | {:<6} |".format(r.nome, r.fabricante, r.modelo))
print()

# Nome e idade das pessoas que possuem um Fiat Mobi
rows = session.query(Pessoa.nome, Pessoa.idade).filter(Pessoa.id_veiculo == Veiculo.id, Veiculo.modelo == "Mobi")
print("Nome e idade das pessoas que possuem um Fiat Mobi: ")
for r in rows:
  print("| {:<7} | {} |".format(r.nome, r.idade))
print()

# Identifique a pessoa mais velha e mostre todos os dados dela e do veículo
rows = session.query(Pessoa.nome, db.func.max(Pessoa.idade).label("idade"), Pessoa.salario, Pessoa.sexo, Veiculo.fabricante, Veiculo.modelo, Veiculo.ano)

for r in rows:
  print()
  print("Identifique a pessoa mais velha e mostre todos os dados dela e do veículo: ")
  print("| {} | {} | {} | {} | {} | {} | {} |".format(r.nome, r.idade, r.salario, r.sexo, r.fabricante, r.modelo, r.ano))

session.commit()
session.close()
conn.close()
