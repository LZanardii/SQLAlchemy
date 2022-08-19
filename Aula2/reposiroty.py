from dataclasses import replace
import sqlalchemy as db
import sqlalchemy.orm as orm
from model import *

engine = db.create_engine(DATABASE_CONNECTION)
conn = engine.connect()

Session = orm.sessionmaker(bind=engine)
session = Session()

# Listagem com nome da pessoa, fabricante e modelo do veículo que ela possui, ordenado pelo nome da pessoa
select = session.query(Pessoa.nome, Veiculo.fabricante, Veiculo.modelo).join(Veiculo).all()
print("\n".join(map(str, select)))

print()

# Listagem com nome da pessoa, fabricante e modelo do veículo que ela possui, ordenado pelo nome da pessoa
select = session.query(Pessoa.nome, Pessoa.idade).join(Veiculo).filter(Veiculo.modelo == "Mobi").all()
print("\n".join(map(str, select)))

print()

#Crie o veículo Hyundai HB20 ano 2021 e o vincule à pessoa “Camila”
# pessoa = session.query(Pessoa).filter(Pessoa.nome == "Camila").first()
# hb20 = Veiculo(modelo = "HB20", fabricante = "Hyundai", ano = "2021", id_pessoa = pessoa.id)
# session.add(hb20)

# Listagem Camila e seus veiculos
select = session.query(Pessoa).join(Veiculo).filter(Pessoa.nome == "Camila").all()
for pessoa in select:
  print("| {} | {} | {} | {} |".format(pessoa.nome, pessoa.idade, pessoa.salario, pessoa.sexo))
  for veiculo in pessoa.veiculos:
    print("| {} | {} | {} |".format(veiculo.fabricante, veiculo.modelo, veiculo.ano))

print()

print("Digite o nome da Pessoa a ser deletada")
nome = input()
pessoa_to_delete = session.query(Pessoa).filter(Pessoa.nome == nome).first()
while (not pessoa_to_delete):
  print()
  print("Pessoa não encontrada, digite outro nome")
  nome = input()
  pessoa_to_delete = session.query(Pessoa).filter(Pessoa.nome == nome).first()
  
if pessoa_to_delete:
  try:
    session.delete(pessoa_to_delete)
    print("Pessoa deletada com sucesso")
  except:
    print()
    print("Erro ao deletar pessoa")

session.commit()
session.close()
conn.close()
