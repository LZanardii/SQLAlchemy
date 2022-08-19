from ast import Load
from orm_model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True

# SELECT uma tabela - Lazy loading
# rows = session.query(Student).all()
# for r in rows:
#     print(r)

# SELECT várias tabelas - Erro cartesiano
# rows = session.query(Student, Address).all()
# for s, a in rows:
#     print(s)

# SELECT várias tabelas - Junção manual no WHERE
# rows = session.query(Student, Address).where(Student.id == Address.student_id).all()
# for s, a in rows:
#     print(s)

# SELECT várias tabelas - Junção automática com JOIN
# rows = session.query(Student).join(Address).all()
# for r in rows:
#     print(r)

# SELECT - Filtro tabela principal
# rows = session.query(Student).where(Student.sex.in_(['f', 'F'])).all()
# for r in rows:
#     print(r)

# SELECT - Filtro tabela secundaria - Erro cruzamento cartesiano
# rows = session.query(Student).where(Address.address == 'Rua das Rosas').all()
# for r in rows:
#     print(r)

# SELECT - Filtro tabela secundaria - Junção automática com JOIN
# rows = session.query(Student).join(Address).where(Address.address == 'Rua das Rosas').all()
# for r in rows:
#     print(r)

# SELECT uma tabela - Junção automática com JOIN - Eager Loading
# rows = session.query(Student).options(orm.joinedload(Student.addresses)).all()
# for r in rows:
#     print(r)

engine.echo=False

# Encerra a conexão com o banco de dados
session.close()
conn.close()
engine.dispose()