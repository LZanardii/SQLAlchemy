from orm_model import *
from sqlalchemy.sql import func

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True

# DELETE um objeto
# row = session.query(Student).where(Student.name == 'Renato').first()
# session.delete(row)

# DELETE vários objetos
# rows = session.query(Student).where(Student.sex == 'F').all()
# for r in rows:
#     session.delete(r)

session.commit()
engine.echo=False

# Encerra a conexão com o banco de dados
session.close()
conn.close()
engine.dispose()