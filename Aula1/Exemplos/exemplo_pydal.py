from pydal import DAL, Field
db = DAL('sqlite://dal_db.db')
db.define_table('mobilia', Field('nome', 'string'))
db.mobilia.insert(nome='Cama')
db.mobilia.insert(nome='Mesa')
db.mobilia.insert(nome='Banco')
db.mobilia.insert(nome='Cadeira')
db.commit()

query = db.mobilia.nome.startswith('C')
rows = db(query).select(orderby=db.mobilia.nome)
for r in rows:
 print(r.id, r.nome)
db.close()
