"""cargar categoria docentes

Revision ID: 64590e4a0e91
Revises: 8a9b4bb6886e
Create Date: 2021-10-05 22:25:10.855318

"""
from alembic import op
import sqlalchemy as sa
from typing import List
from app.models.core.modelos_principales import CategoriaDocenteLOSEP
from sqlalchemy.sql.expression import delete, select
from sqlalchemy.orm.session import Session


# revision identifiers, used by Alembic.
revision = '64590e4a0e91'
down_revision = '8a9b4bb6886e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    categorias = [
        'CATEGORIA 1',
        'CATEGORIA 2',
        'CATEGORIA 3',
        'CATEGORIA 4',
        'CATEGORIA 5',
        'NO APLICA'
    ]

    session = Session(bind=op.get_bind())
    lista: List[CategoriaDocenteLOSEP] = []
    for categoria in categorias:
        
        results = session.execute(
            select(CategoriaDocenteLOSEP).where(CategoriaDocenteLOSEP.categoria_docente==categoria)
        )
        existe = results.all()
        if existe:
            break
        lista.append(CategoriaDocenteLOSEP(categoria_docente=categoria))
        
    session.add_all(lista)
    session.commit()
        
    session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session = Session(bind=op.get_bind())
    session.execute(delete(CategoriaDocenteLOSEP))
    session.commit()
    session.close()
    # ### end Alembic commands ###
