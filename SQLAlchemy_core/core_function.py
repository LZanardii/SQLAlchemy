from core_model import *
from sqlalchemy.sql import func

# print('\nCURRENT TIMESTAMP')
# query = db.select(func.now())
# print(conn.execute(query).fetchone())

# print('\nSELECT COUNT')
# query = db.select(func.count(students.c.id).label('qt'))
# print(conn.execute(query).fetchone())

# print('\nSELECT COUNT DISTINCT')
# query = db.select(func.count(students.c.sex.distinct()))
# print(conn.execute(query).fetchone())

print('\nSELECT STATS FUNCTIONS')
query = db.select([
    func.min(students.c.age).label('min'),
    func.max(students.c.age).label('max'),
    func.sum(students.c.age).label('sum'),
    func.count(students.c.age).label('count'),
    func.avg(students.c.age).label('avg')])
result = conn.execute(query)
for k, v in zip(result.keys(), result.fetchone()):
    print(k, '\t', v)

# print('\nSELECT STRING FUNCTIONS')
# query = db.select([
#     func.lower(students.c.name),
#     func.upper(students.c.lastname)])
# print(conn.execute(query).fetchall())

# Encerra a conexão com o banco de dados
conn.close()
engine.dispose()
