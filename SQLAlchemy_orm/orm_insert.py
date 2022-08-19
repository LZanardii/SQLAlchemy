from orm_model import *

Session = orm.sessionmaker(bind=engine)
session = Session()

# Insert
try:
    s1 = Student(name='Marcos', lastname='Pereira', sex='M', age=41)
    a1 = Address(address='Rua das Acácias', email='marcos@gmail.com')
    s1.addresses = [a1]

    s2 = Student(
        name='Sandra', lastname='Matos', sex='F', age=29,
        addresses=[Address(address='Rua das Rosas', email='sandra@gmail.com')])

    s3 = Student(
        name='Vitor', lastname='Leite', sex='M', age=36,
        addresses=[
            Address(address='Rua dos Cravos', email='vitor@gmail.com'),
            Address(address='Rua dos Cedros', email='vitorleite@gmail.com')])

    s4 = [
        Student(
            name='Bianca', lastname='Santos', sex='F', age=18,
            addresses=[Address(address='Rua das Camélias', email='bianca@gmail.com')]),

        Student(
            name='Renato', lastname='Assis', sex='M', age=22,
            addresses=[Address(address='Rua das Papoulas', email='renato@gmail.com')])
    ]

    session.add(s1)
    session.add(s2)
    session.add(s3)
    session.add_all(s4)
    session.commit()
except Exception as e:
    session.rollback()
    print(e)

# Encerra a conexão com o banco de dados
session.close()
conn.close()
engine.dispose()