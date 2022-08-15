from core_model import *

# print('\nCRUZAMENTO CARTESIANO')
# query = db.select([students, addresses]).where(students.c.id == addresses.c.student_id)
# result = conn.execute(query)
# for row in result:
#    print(row)

# print('\nJOIN COMPLETO')
# query = db.select([students, addresses]).join(addresses, students.c.id == addresses.c.student_id)   
# result = conn.execute(query)
# for row in result:
#    print(row)

# print('\nJOIN COM PROJECAO')
# query = db.select([students.c.name, addresses.c.email]).join(addresses, students.c.id == addresses.c.student_id)   
# result = conn.execute(query)
# for row in result:
#    print(row)

# print('\nJOIN COM PROJECAO E FILTRO')
# query = db.select([students.c.name, addresses.c.email]).where(students.c.sex == 'M').join(addresses, students.c.id == addresses.c.student_id)   
# result = conn.execute(query)
# for row in result:
#    print(row)

# Encerra a conexão com o banco de dados
conn.close()
engine.dispose()