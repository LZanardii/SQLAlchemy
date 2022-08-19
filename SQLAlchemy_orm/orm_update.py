from orm_model import *
from sqlalchemy.sql import func

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True

# UPDATE direto no banco
# session.query(Student).where(Student.sex == 'M').update({Student.sex:'m'})

# UPDATE via objetos
# rows = session.query(Student).where(Student.sex == 'F').all()
# for r in rows:
#     r.sex = 'f'

session.commit()
engine.echo=False

# Encerra a conexão com o banco de dados
session.close()
conn.close()
engine.dispose()