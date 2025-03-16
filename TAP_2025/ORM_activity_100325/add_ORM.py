from ORM_test import engine, Post
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
sesion = Session()

for t in range(1,40):
    try:
        tr=Post(t,"Un mensaje cualquiera", "Anonimo")
        sesion.add(tr)
    except:
        print("Error al intentar insertar un registro")

sesion.commit()