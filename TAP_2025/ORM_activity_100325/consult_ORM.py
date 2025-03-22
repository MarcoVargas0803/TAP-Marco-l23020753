import ORM_test
from ORM_test import Post
from  sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=ORM_test.engine)
session = Session()

"""
#Equivalente a SELECT from * fROM demo
resultado = session.query(Post).all()
for s in resultado:
    print(s)
"""

#Equivalente a consultar por filtrado WHERE
#En este caso consultamos donde el registro sea igual 20.
"""
res = session.query(Post).filter_by(id=20)
for s in res:
    print(s.id,s.mensaje,s.autor)
"""

#Equivalente a filtrar los registros menores a id<20

"""
res=session.query(Post).filter(Post.id<20)
for s in res:
    print(s.id,s.mensaje,s.autor)
"""

#Filtrado combinado entre id > 10 & id < 20

"""
res=session.query(Post).filter(Post.id<20).filter(Post.id>10)
for s in res:
    print(s.id,s.mensaje,s.autor)
"""

#Consultar ultimo Id de la base de datos
ultimo_registro = session.query(Post).order_by(Post.id.desc()).first()
ultimo_id = ultimo_registro.id if ultimo_registro else None

print(f"Último ID: {ultimo_id}")