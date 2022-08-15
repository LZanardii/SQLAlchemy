from core_model import *
from sqlalchemy.sql import func
import sqlalchemy.orm as orm

print('\nUPDATE SEM SESSION')
# Constante
query = students.update().where(students.c.sex == 'F').values(sex='f')

# Executa e retorna quantidade de linhas
print('Linhas atualizadas:', conn.execute(query).rowcount)

# Session = orm.sessionmaker(bind=engine)
# session = Session()

# print('\nUPDATE COM SESSION')
# Constante
# query = students.update().where(students.c.sex == 'M').values(sex='m')

# Fórmula
# query = students.update().where(students.c.age > 30).values(age=students.c.age + 1)

# Função
# query = students.update().where(students.c.sex == 'F').values(sex=func.lower(students.c.sex))

# Executa e retorna quantidade de linhas
# print('Linhas atualizadas:', session.execute(query).rowcount)

# Encerra a conexão com o banco de dados
# session.commit()
# session.rollback()
# session.close()
conn.close()
engine.dispose()
