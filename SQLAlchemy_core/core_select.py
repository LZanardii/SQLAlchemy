from core_model import *

# print('\nSELECT ALL')
# query = students.select()
# result = conn.execute(query)
# for row in result:
#    print(row)

# print('\nSELECT COLUMNS')
# query = db.select(students.c.sex)
# print(conn.execute(query).fetchall())

# print('\nSELECT DISTINCT')
# query = db.select(students.c.sex).distinct()
# print(conn.execute(query).fetchall())

# print('\nSELECT ORDER BY ASC/DESC')
# query = db.select([students.c.name, students.c.age]).order_by(students.c.age.desc())
# print(conn.execute(query).fetchall())

# print('\nSELECT WHERE sex = M')
# query = students.select().where(students.c.sex == 'M')
# print(', '.join([s.name for s in conn.execute(query).fetchall()]))

# print('\nSELECT WHERE name LIKE "_a%"')
# query = students.select().where(students.c.name.ilike('_a%'))
# print(', '.join([s.name for s in conn.execute(query).fetchall()]))

# print('\nSELECT WHERE AND')
# query = students.select().where((students.c.sex == 'M') & (students.c.age > 25))
# print(conn.execute(query).fetchall())

# print('\nSELECT WHERE OR')
# query = students.select().where((students.c.age < 20) | (students.c.age > 30))
# print('\n'.join([s.name + '\t' + str(s.age) for s in conn.execute(query).fetchall()]))

# print('\nSELECT WHERE BETWEEN')
# query = students.select().where(students.c.age.between(20, 30))
# print('\n'.join([s.name + '\t' + str(s.age) for s in conn.execute(query).fetchall()]))

# print('\nSELECT WHERE IN')
# query = students.select().where(students.c.id.in_([1, 3, 5]))
# print('\n'.join([str(s.id) + '\t' + s.name for s in conn.execute(query).fetchall()]))

# print('\nCUSTOM SELECT')
# query = db.text('SELECT lastname FROM student WHERE lastname LIKE :last ORDER BY lastname')
# result = conn.execute(query, last='%s')
# print(', '.join([s[0] for s in result.fetchall()]))

# Encerra a conexão com o banco de dados
conn.close()
engine.dispose()
