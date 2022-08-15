from core_model import *
from sqlalchemy.sql import func

# print('\nSELECT GROUP BY')
# query = db.select([func.count(students.c.id), students.c.sex]).group_by(students.c.sex)
# print(conn.execute(query).fetchall())

# print('\nSELECT GROUP BY HAVING')
# query = db.select([
#     func.count(students.c.id), students.c.sex]) \
#     .group_by(students.c.sex) \
#     .having(func.count(students.c.id) > 2)
# print(conn.execute(query).fetchall())

# Encerra a conexão com o banco de dados
conn.close()
engine.dispose()
