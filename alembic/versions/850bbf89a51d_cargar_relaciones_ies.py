"""cargar relaciones ies

Revision ID: 850bbf89a51d
Revises: ea676797411f
Create Date: 2021-10-05 21:14:05.644474

"""
from typing import List
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import delete, select
from app.models.core.modelos_principales import RelacionIES

# revision identifiers, used by Alembic.
revision = '850bbf89a51d'
down_revision = 'ea676797411f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    relaciones = [
        'NOMBRAMIENTO',
        'CONTRATO CON RELACION DE DEPENDENCIA',
        'CONTRATO SIN RELACION DE DEPENDENCIA',
        'PROMETEO'
    ]
    session = Session(bind=op.get_bind())
    lista: List[RelacionIES] = []
    
    for relacion in relaciones:
        resluts = session.execute(
            select(RelacionIES).where(relacion==relacion)
        )
        existe = resluts.all()
        if existe:
            break
        lista.append(RelacionIES(relacion=relacion))
    session.add_all(lista)
    session.commit()
    session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session = Session(bind=op.get_bind())
    session.execute(delete(RelacionIES))
    session.commit()
    session.close()
    # ### end Alembic commands ###
