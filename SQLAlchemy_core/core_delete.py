from core_model import *
from sqlalchemy.sql import func
import sqlalchemy.orm as orm

# print('\nDELETE SEM SESSION')
# TRUNCATE
# query = students.delete()

# Executa e retorna quantidade de linhas
# print('Linhas removidas:', conn.execute(query).rowcount)

Session = orm.sessionmaker(bind=engine)
session = Session()

print('\nDELETE COM SESSION')

# TRUNCATE
query = students.delete()

# WHERE
# query = students.delete().where(students.c.age < 25)

# Executa e retorna quantidade de linhas
print('Linhas removidas:', session.execute(query).rowcount)

# Encerra a conexão com o banco de dados
# session.commit()
session.rollback()
session.close()
conn.close()
engine.dispose()
