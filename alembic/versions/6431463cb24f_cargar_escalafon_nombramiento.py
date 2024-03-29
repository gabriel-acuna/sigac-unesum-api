"""cargar escalafon nombramiento

Revision ID: 6431463cb24f
Revises: 850bbf89a51d
Create Date: 2021-10-05 21:32:50.984129

"""
from typing import List
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import delete, select
from app.models.core.modelos_principales import TipoEscalafonNombramiento


# revision identifiers, used by Alembic.
revision = '6431463cb24f'
down_revision = '850bbf89a51d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    escalafones = [
        'LABORAL PREVIO',
        'LABORAL ACTUAL',
        'NO APLICA'
    ]

    session = Session(bind=op.get_bind())
    lista: List[TipoEscalafonNombramiento] = []
    for escalafon in escalafones:
        
        results = session.execute(
            select(TipoEscalafonNombramiento).where(TipoEscalafonNombramiento.escalafon_nombramiento==escalafon)
        )
        existe = results.all()
        if existe:
            break
        lista.append(TipoEscalafonNombramiento(escalafon_nombramiento=escalafon))
        
    
    
    session.add_all(lista)
    session.commit()
        
    session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session = Session(bind=op.get_bind())
    session.execute(delete(TipoEscalafonNombramiento))
    session.commit()
    session.close()
    # ### end Alembic commands ###
