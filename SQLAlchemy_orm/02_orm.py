import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///orm_db.db', echo=False)
conn = engine.connect()

Base = orm.declarative_base()


class Mobilia(Base):
    __tablename__ = 'mobilia'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)


Base.metadata.create_all(engine)

Session = orm.sessionmaker(bind=engine)
session = Session()

rows = [Mobilia(nome="Cama"), Mobilia(nome="Mesa"),
        Mobilia(nome="Banco"), Mobilia(nome="Cadeira")]

session.add_all(rows)
session.commit()

rows = session.query(Mobilia).where(
    Mobilia.nome.startswith('C')).order_by(Mobilia.nome).all()

for r in rows:
    print(r.id, r.nome)

session.close()
conn.close()
