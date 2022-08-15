from core_model import *

# Objeto que gerencia os metadados do banco de dados
meta.reflect(bind=engine)

# Percorre todas as tabelas
for tname, table in meta.tables.items():
  print('\nEstrutura da tabela', tname)
  print(repr(table))
  
  print('\nDados da tabela', tname)
  for row in engine.execute(table.select()):
    print(row)

# Encerra a conexão com o banco de dados
conn.close()
engine.dispose()