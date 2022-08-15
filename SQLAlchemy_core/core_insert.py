from core_model import *

# Insert
try:
    result_proxy = conn.execute(students.insert().values(
        name='Marcos', lastname='Pereira', sex='M', age=41))
    print('id:', result_proxy.inserted_primary_key)

    result_proxy = conn.execute(students.insert(), [
        {'name': 'Sandra', 'lastname': 'Matos', 'sex': 'F', 'age': 29},
        {'name': 'Vitor', 'lastname': 'Leite', 'sex': 'M', 'age': 36},
        {'name': 'Bianca', 'lastname': 'Santos', 'sex': 'F', 'age': 18},
        {'name': 'Renato', 'lastname': 'Assis', 'sex': 'M', 'age': 22},
    ])
    print('ids:', result_proxy.inserted_primary_key_rows)

    result_proxy = conn.execute(addresses.insert(), [
        {'student_id': 1, 'address': 'Rua das Acácias', 'email': 'marcos@gmail.com'},
        {'student_id': 2, 'address': 'Rua das Rosas', 'email': 'sandra@gmail.com'},
        {'student_id': 3, 'address': 'Rua dos Cravos', 'email': 'vitor@gmail.com'},
        {'student_id': 4, 'address': 'Rua das Camélias', 'email': 'bianca@gmail.com'},
        {'student_id': 5, 'address': 'Rua das Papoulas', 'email': 'renato@gmail.com'},
    ])
    print('ids:', result_proxy.inserted_primary_key_rows)

except Exception as e:
    print(e)

# Encerra a conexão com o banco de dados
conn.close()
engine.dispose()